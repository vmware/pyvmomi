
vim.vm.device.VirtualController
===============================
  VirtualController is the base data object type for a device controller in a virtual machine. VirtualController extends `VirtualDevice <vim/vm/device/VirtualDevice.rst>`_ to inherit general information about a controller (such as name and description), and to allow controllers to appear in a generic list of virtual devices.
:extends: vim.vm.device.VirtualDevice_

Attributes:
    busNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Bus number associated with this controller.
    device ([`int <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       List of devices currently controlled by this controller. Each entry contains the `key <vim/vm/device/VirtualDevice.rst#key>`_ property of the corresponding device object.
