vim.vm.device.VirtualDeviceOption.URIBackingOption.Direction
============================================================
  TheVirtualDeviceURIBackingOptionDirectionenum type provides values for the direction of a network connection.
  :contained by: `vim.vm.device.VirtualDeviceOption.URIBackingOption <vim/vm/device/VirtualDeviceOption/URIBackingOption.rst>`_

  :type: `vim.vm.device.VirtualDeviceOption.URIBackingOption.Direction <vim/vm/device/VirtualDeviceOption/URIBackingOption/Direction.rst>`_

  :name: client

values:
--------

client
   Indicates that the virtual machine can initiate a connection with a system on the network using the specified `serviceURI <vim/vm/device/VirtualDevice/URIBackingInfo.rst#serviceURI>`_ .

server
   Indicates that the virtual machine can listen for a connection on the specified `serviceURI <vim/vm/device/VirtualDevice/URIBackingInfo.rst#serviceURI>`_ .
