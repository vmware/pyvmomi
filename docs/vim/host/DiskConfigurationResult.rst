.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _ScsiDisk: ../../vim/host/ScsiDisk.rst

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.host.DiskConfigurationResult
================================
  Disk configuration result returns success or fault of the operation on the disk.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    devicePath (`str`_, optional):

       The device path. See `ScsiDisk`_ 
    success (`bool`_, optional):

       Flag to indicate if the operation is successful
    fault (`vmodl.LocalizedMethodFault`_, optional):

       'fault' would be set if the operation was not successful
