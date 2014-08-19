
vim.vApp.OvfSectionInfo
=======================
  The OvfSection encapsulates uninterpreted meta-data sections in an OVF descriptor. When an OVF package is imported, non-required / non-interpreted sections will be stored as OvfSection object. During the creation of an OVF package, these sections will be placed in the OVF descriptor.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       A unique key to identify a section.
    namespace (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The namespace for the value in xsi:type attribute.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The value of the xsi:type attribute not including the namespace prefix.
    atEnvelopeLevel (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether this is a global envelope section
    contents (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The XML fragment including the top-levelSection...element. The fragment is self-contained will all required namespace definitions.
