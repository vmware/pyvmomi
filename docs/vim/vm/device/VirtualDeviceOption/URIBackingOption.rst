.. _client: ../../../../vim/vm/device/VirtualDeviceOption/URIBackingOption/Direction.rst#client

.. _server: ../../../../vim/vm/device/VirtualDeviceOption/URIBackingOption/Direction.rst#server

.. _vSphere API 4.1: ../../../../vim/version.rst#vimversionversion6

.. _vim.option.ChoiceOption: ../../../../vim/option/ChoiceOption.rst

.. _vim.vm.device.VirtualDeviceOption.BackingOption: ../../../../vim/vm/device/VirtualDeviceOption/BackingOption.rst


vim.vm.device.VirtualDeviceOption.URIBackingOption
==================================================
  The URIBackingOption data object type describes network communication options for virtual devices. When establishing a connection with a remote system on the network, the virtual machine can act as a server or a client. When the virtual machine acts as a server, it accepts a connection. When the virtual machine acts as a client, it initiates the connection.
:extends: vim.vm.device.VirtualDeviceOption.BackingOption_
:since: `vSphere API 4.1`_

Attributes:
    directions (`vim.option.ChoiceOption`_):

       List of possible directions. Valid directions are:
        * `server`_
        * 
        * `client`_
        * 
        * 
