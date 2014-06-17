.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.TargetInfo: ../../vim/vm/TargetInfo.rst


vim.vm.ScsiPassthroughInfo
==========================
  Description of a generic SCSI device, including information about the device ID.
:extends: vim.vm.TargetInfo_

Attributes:
    scsiClass (`str`_):

       The class of the generic SCSI device.
    vendor (`str`_):

       The vendor name.
    physicalUnitNumber (`int`_):

       Unit number of the generic device on the physical host.
