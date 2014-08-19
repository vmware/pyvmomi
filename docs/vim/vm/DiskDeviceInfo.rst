
vim.vm.DiskDeviceInfo
=====================
  The DiskDeviceInfo class contains basic information about a specific disk hardware device.
:extends: vim.vm.TargetInfo_

Attributes:
    capacity (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Size of disk
    vm ([`vim.VirtualMachine <vim/VirtualMachine.rst>`_], optional):

       List of known virtual machines using this physical disk as a backing
