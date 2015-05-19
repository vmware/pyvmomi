.. _vim.BoolPolicy: ../../../vim/BoolPolicy.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.InheritablePolicy: ../../../vim/InheritablePolicy.rst


vim.dvs.VmwareDistributedVirtualSwitch.SecurityPolicy
=====================================================
  This data object type describes security policy governing ports.
:extends: vim.InheritablePolicy_
:since: `vSphere API 4.0`_

Attributes:
    allowPromiscuous (`vim.BoolPolicy`_, optional):

       The flag to indicate whether or not all traffic is seen on the port.
    macChanges (`vim.BoolPolicy`_, optional):

       The flag to indicate whether or not the Media Access Control (MAC) address can be changed.
    forgedTransmits (`vim.BoolPolicy`_, optional):

       The flag to indicate whether or not the virtual network adapter should be allowed to send network traffic with a different MAC address than that of the virtual network adapter.
