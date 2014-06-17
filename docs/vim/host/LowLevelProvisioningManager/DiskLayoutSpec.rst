.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.LowLevelProvisioningManager.DiskLayoutSpec
===================================================
  File layout spec of a virtual disk. The disk could be either a base-disk or a delta disk.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    controllerType (`str`_):

       Disk controller type, e.g. vim.vm.device.VirtualSCSIController or vim.vm.device.VirtualIDEController.
    busNumber (`int`_):

       Bus number associated with the controller for this disk.
    unitNumber (`int`_):

       Unit number of this disk on its controller.
    srcFilename (`str`_):

       Source disk filename in datastore path.
    dstFilename (`str`_):

       Destination filename in datastore path.
