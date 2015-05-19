.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.OvfConsumer.OstNode: ../../vim/OvfConsumer/OstNode.rst

.. _vim.OvfConsumer.OvfSection: ../../vim/OvfConsumer/OvfSection.rst


vim.OvfConsumer.OstNode
=======================
  A node in the OVF section tree.This class represents a node on which OVF sections can be defined. The possible node types are OstNodeType.envelope, OstNodeType.virtualSystem or OstNodeType.virtualSystemCollection, corresponding to the identically named OVF element types.Since the node contains a list of children, it can also be regarded as a tree. This tree mirrors the structure of the OVF descriptor. It is provided to OVF consumers as a more convenient way to navigate and modify the OVF than by working directly on the XML.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    id (`str`_):

       The OVF id of the Content (VirtualSystem or VirtualSystemCollection) element. Empty on the envelope node.
    type (`str`_):

       The type of the node. Possible values are defined in the OstNodeType enum.Since the OstNode tree structure mirrors the structure of the OVF descriptor, only one Envelope node is defined, and it is always the root of the tree.
    section ([`vim.OvfConsumer.OvfSection`_], optional):

       The list of sections on this node.
    child ([`vim.OvfConsumer.OstNode`_], optional):

       The list of child nodes. As dictated by OVF, this list is subject to the following rules:
        * The Envelope node must have exactly one child.
        * VirtualSystemCollection nodes may have zero or more children.
        * VirtualSystem nodes must have no children.
    entity (`vim.ManagedEntity`_, optional):

       The VM or vApp corresponding to this node.This field is set when this OstNode represents an existing managed entity.The entity is unset on nodes of type OstNodeType.envelope.
