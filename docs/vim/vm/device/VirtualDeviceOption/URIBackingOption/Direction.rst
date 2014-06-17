.. _serviceURI: ../../../../../vim/vm/device/VirtualDevice/URIBackingInfo.rst#serviceURI

.. _vim.vm.device.VirtualDeviceOption.URIBackingOption: ../../../../../vim/vm/device/VirtualDeviceOption/URIBackingOption.rst

.. _vim.vm.device.VirtualDeviceOption.URIBackingOption.Direction: ../../../../../vim/vm/device/VirtualDeviceOption/URIBackingOption/Direction.rst

vim.vm.device.VirtualDeviceOption.URIBackingOption.Direction
============================================================
  TheVirtualDeviceURIBackingOptionDirectionenum type provides values for the direction of a network connection.
  :contained by: `vim.vm.device.VirtualDeviceOption.URIBackingOption`_

  :type: `vim.vm.device.VirtualDeviceOption.URIBackingOption.Direction`_

  :name: client

values:
--------

client
   Indicates that the virtual machine can initiate a connection with a system on the network using the specified `serviceURI`_ .

server
   Indicates that the virtual machine can listen for a connection on the specified `serviceURI`_ .
