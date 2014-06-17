.. _int: https://docs.python.org/2/library/stdtypes.html

.. _VirtualDevice: ../../../vim/vm/device/VirtualDevice.rst

.. _vim.vm.device.VirtualDevice: ../../../vim/vm/device/VirtualDevice.rst


vim.vm.device.VirtualController
===============================
  VirtualController is the base data object type for a device controller in a virtual machine. VirtualController extends `VirtualDevice`_ to inherit general information about a controller (such as name and description), and to allow controllers to appear in a generic list of virtual devices.
:extends: vim.vm.device.VirtualDevice_

Attributes:
    busNumber (`int`_):

       Bus number associated with this controller.
    device (`int`_, optional):

       List of devices currently controlled by this controller. Each entry contains the `key`_ property of the corresponding device object.
