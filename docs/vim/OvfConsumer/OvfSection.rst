
vim.OvfConsumer.OvfSection
==========================
  A self-contained OVF section
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    lineNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The line number in the OVF descriptor on which this section starts.The line number is only present on sections that were imported as part of an OVF descriptor (as opposed to sections that are about to be exported to OVF).The value is zero if the section did not originate from an OVF descriptor.
    xml (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The XML fragment for the section.The XML fragment must explicitly define all namespaces and namespace prefixes that are used in the fragment, including the default namespace.
