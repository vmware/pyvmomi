.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.ExtensionManager.IpAllocationUsage
======================================
  This data object type contains usage information about an extension's IP allocation usage.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    extensionKey (`str`_):

       Key of the extension whose usage is being reported.
    numAddresses (`int`_):

       Number of IP addresses allocated from IP pools.
