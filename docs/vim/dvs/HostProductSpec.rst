
vim.dvs.HostProductSpec
=======================
  This data object type is a subset of `AboutInfo <vim/AboutInfo.rst>`_ . An object of this type can be used to describe the specification for a host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    productLineId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The product-line name.
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Dot-separated version string. For example, "1.2".
