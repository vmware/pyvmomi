# VMware vSphere Python SDK
# Copyright (c) 2008-2014 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from lxml import etree

from pyVmomi.SoapAdapter import SOAP_NSMAP


# inverted map from the soap adapter for use with lxml etree
NSMAP = dict(zip(SOAP_NSMAP.values(), SOAP_NSMAP.keys()))


# derive a list of all attributes in both nodes
def _extract_attribute_names(expected, observed):
    names = set()
    for name in expected.attrib:
        names.add(name)
    for name in observed.attrib:
        names.add(name)
    return names


# returns without exception if both nodes have identical attribute lists
def _check_attribute_names(expected, observed, names):
    for name in names:
        assert name in expected.attrib.keys()
        assert name in observed.attrib.keys()
    return True


# returns without exception only if the attributes on both nodes match
def _check_attribute_values(expected, observed, names):
    for name in names:
        e_val = expected.attrib[name]
        o_val = observed.attrib[name]
        assert e_val == o_val
    return True


# returns only if the attributes on both nodes check out
def _attribute_compare(expected, observed):
    names = _extract_attribute_names(expected, observed)
    _check_attribute_names(expected, observed, names)
    _check_attribute_values(expected, observed, names)
    return True


# returns only if the current nodes match tag, text, and attributes
def _node_compare(expected, observed):
    assert expected.tag == observed.tag
    assert expected.text == observed.text
    return _attribute_compare(expected, observed)


# returns True only if both trees match completely
def _compare_node_lists(expected_nodes, observed_nodes, comparison):
    assert len(expected_nodes) == len(observed_nodes)
    match = True
    for e, o in zip(expected_nodes, observed_nodes):
        match = match and _attribute_compare(e, o) and _compare(e, o,
                                                               comparison)
    return match


# compares trees based on comparison method passed in
def _compare(expected, observed, comparison):
    tags = set()
    for child in expected:
        tags.add(child.tag)
    for child in observed:
        tags.add(child.tag)

    for tag in tags:
        elist = expected.findall(tag)
        olist = observed.findall(tag)
        _compare_node_lists(elist, olist, comparison)

    return comparison(expected, observed)


def full_compare(expected, observed):
    """Performs a logical comparison of two XML documents.

    The first document is used to confirm the second.

    Args:
        expected (str): The expected XML document as a string.
        observed (str): The observed XML document as a string.

    Returns:
        bool. If the documents match or do not.
    """
    exp = etree.XML(expected)
    obs = etree.XML(observed)

    try:
        return _compare(exp, obs, _node_compare)
    except AssertionError:
        return False


# trims off the <?xml version="1.0" encoding="UTF-8"?> tag and whitespace
def _trim_encoding_declaration(source):
    index = source.index('?>')
    return source[index+3:].strip()


def soap_compare(expected, observed):
    """Compares two soap documents based on their XML trees.

    Returns true only if both trees are logically equivalent.
    """
    etrimmed = _trim_encoding_declaration(expected)
    otrimmed = _trim_encoding_declaration(observed)
    return full_compare(etrimmed, otrimmed)


# searching in SOAP documents requires knowledge of the XML namespace
def _soap_search_for_tag(doc, tag):
    search = './/{0}'.format(tag)
    return doc.findall(search, namespaces=NSMAP)


# searching in non-soap documents does not require namespace knowledge
def _search_for_tag(doc, tag):
    search = './/{0}'.format(tag)
    return doc.findall(search)


def _node_comparator(list_a, list_b, comparator):
    try:
        return _compare_node_lists(list_a, list_b, comparator)
    except AssertionError:
        return False


def node_wise(expected, observed, tag_name):
    """Performs a logical comparison of two XML documents restricted by node.

    NOTE: only top-level nodes under root node can be used because of a
    limitation in Python 2.6 which prevents us from searching for tags deeper
    than the top level.

    The first document confirms the second but only as far as the named
    nodes in the document with the name `tag_name` are concerned.

    Args:
        expected (str): The expected XML document as a string.
        observed (str): The observed XML document as a string.
        tag_name (str): The name of the tag(s) you want to assert are the same.

    Returns:
        bool. If the documents match or do not.
    """
    exp = etree.XML(expected)
    obs = etree.XML(observed)

    expected_nodes = _search_for_tag(exp, tag_name)
    observed_nodes = _search_for_tag(obs, tag_name)

    return _node_comparator(expected_nodes, observed_nodes, _node_compare)


def soap_node_wise(expected, observed, tag_name):
    """Performs a logical comparison of two SOAP documents restricted by node.

    Slightly different internal details handle namespace related issues with
    searching within a SOAP envelope.

    Args:
        expected (str): The expected XML document as a string.
        observed (str): The observed XML document as a string.
        tag_name (str): The name of the tag(s) you want to assert are the same.

    Returns:
        bool. If the documents match or do not.
    """
    etrimmed = _trim_encoding_declaration(expected)
    otrimmed = _trim_encoding_declaration(observed)

    exp = etree.XML(etrimmed)
    obs = etree.XML(otrimmed)

    expected_nodes = _soap_search_for_tag(exp, tag_name)
    observed_nodes = _soap_search_for_tag(obs, tag_name)

    return _node_comparator(expected_nodes, observed_nodes, _node_compare)
