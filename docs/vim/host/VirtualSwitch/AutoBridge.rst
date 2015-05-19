.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.host.VirtualSwitch.Bridge: ../../../vim/host/VirtualSwitch/Bridge.rst


vim.host.VirtualSwitch.AutoBridge
=================================
  This data type describes a bridge that automatically selects a particular physical network adapter on the host according to some predetermined policy. Used primarily to support mobility scenarios.
:extends: vim.host.VirtualSwitch.Bridge_

Attributes:
    excludedNicDevice ([`str`_], optional):

       List of physical network adapters that have been excluded from participating in the AutoBridge
