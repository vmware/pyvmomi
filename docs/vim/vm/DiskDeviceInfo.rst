.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.TargetInfo: ../../vim/vm/TargetInfo.rst

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst


vim.vm.DiskDeviceInfo
=====================
  The DiskDeviceInfo class contains basic information about a specific disk hardware device.
:extends: vim.vm.TargetInfo_

Attributes:
    capacity (`long`_, optional):

       Size of disk
    vm ([`vim.VirtualMachine`_], optional):

       List of known virtual machines using this physical disk as a backing
