
vim.vm.device.VirtualPCNet32Option
==================================
  The VirtualPCNet32Option data object type defines the options for the VirtualPCNet32 data object type. Except for the boolean supportsMorphing option, the options are inherited from the `VirtualEthernetCardOption <vim/vm/device/VirtualEthernetCardOption.rst>`_ data object type.
:extends: vim.vm.device.VirtualEthernetCardOption_

Attributes:
    supportsMorphing (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates that this Ethernet card supports morphing into vmxnet when appropriate. This means that, if supportsMorphing="true", the virtual AMD Lance PCNet32 Ethernet card becomes a vmxnet Ethernet card with its added performance capabilities when appropriate.
