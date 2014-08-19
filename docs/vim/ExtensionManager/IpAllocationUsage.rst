
vim.ExtensionManager.IpAllocationUsage
======================================
  This data object type contains usage information about an extension's IP allocation usage.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    extensionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Key of the extension whose usage is being reported.
    numAddresses (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of IP addresses allocated from IP pools.
