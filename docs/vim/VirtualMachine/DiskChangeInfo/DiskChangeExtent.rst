.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.VirtualMachine.DiskChangeInfo.DiskChangeExtent
==================================================
  An area of the disk flagged as modified
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    start (`long`_):

       Start offset (in bytes) of modified area
    length (`long`_):

       Length (in bytes) of modified area
