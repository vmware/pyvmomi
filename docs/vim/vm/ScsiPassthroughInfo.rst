
vim.vm.ScsiPassthroughInfo
==========================
  Description of a generic SCSI device, including information about the device ID.
:extends: vim.vm.TargetInfo_

Attributes:
    scsiClass (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The class of the generic SCSI device.
    vendor (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The vendor name.
    physicalUnitNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Unit number of the generic device on the physical host.
