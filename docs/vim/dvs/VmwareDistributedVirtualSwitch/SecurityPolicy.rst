
vim.dvs.VmwareDistributedVirtualSwitch.SecurityPolicy
=====================================================
  This data object type describes security policy governing ports.
:extends: vim.InheritablePolicy_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    allowPromiscuous (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       The flag to indicate whether or not all traffic is seen on the port.
    macChanges (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       The flag to indicate whether or not the Media Access Control (MAC) address can be changed.
    forgedTransmits (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       The flag to indicate whether or not the virtual network adapter should be allowed to send network traffic with a different MAC address than that of the virtual network adapter.
