.. _vim.host.LinkDiscoveryProtocolConfig: ../../../vim/host/LinkDiscoveryProtocolConfig.rst

.. _vim.host.LinkDiscoveryProtocolConfig.OperationType: ../../../vim/host/LinkDiscoveryProtocolConfig/OperationType.rst

vim.host.LinkDiscoveryProtocolConfig.OperationType
==================================================
  The Discovery Protocol operation.
  :contained by: `vim.host.LinkDiscoveryProtocolConfig`_

  :type: `vim.host.LinkDiscoveryProtocolConfig.OperationType`_

  :name: both

values:
--------

both
   Sent discovery packets for the switch and listen for incoming discovery packets.

none
   Don't listen for incoming discovery packets and don't sent discover packets for the switch either.

advertise
   Sent discovery packets for the switch, but don't listen for incoming discovery packets.

listen
   Listen for incoming discovery packets but don't sent discovery packet for the switch.
