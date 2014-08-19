
vim.vm.device.VirtualDeviceOption.URIBackingOption
==================================================
  The URIBackingOption data object type describes network communication options for virtual devices. When establishing a connection with a remote system on the network, the virtual machine can act as a server or a client. When the virtual machine acts as a server, it accepts a connection. When the virtual machine acts as a client, it initiates the connection.
:extends: vim.vm.device.VirtualDeviceOption.BackingOption_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    directions (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       List of possible directions. Valid directions are:
        * `server <vim/vm/device/VirtualDeviceOption/URIBackingOption/Direction.rst#server>`_
        * 
        * `client <vim/vm/device/VirtualDeviceOption/URIBackingOption/Direction.rst#client>`_
        * 
        * 
