
vim.host.DiskConfigurationResult
================================
  Disk configuration result returns success or fault of the operation on the disk.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    devicePath (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The device path. See `ScsiDisk <vim/host/ScsiDisk.rst>`_ 
    success (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate if the operation is successful
    fault (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_, optional):

       'fault' would be set if the operation was not successful
