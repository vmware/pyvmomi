
vim.host.LowLevelProvisioningManager.DiskLayoutSpec
===================================================
  File layout spec of a virtual disk. The disk could be either a base-disk or a delta disk.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    controllerType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Disk controller type, e.g. vim.vm.device.VirtualSCSIController or vim.vm.device.VirtualIDEController.
    busNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Bus number associated with the controller for this disk.
    unitNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Unit number of this disk on its controller.
    srcFilename (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Source disk filename in datastore path.
    dstFilename (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Destination filename in datastore path.
