vim.dvs.TrafficRule.RuleDirectionType
=====================================
  Network Traffic Rule direction types. It specifies whether rule needs to be applied for packets which are incoming/outgoing or both.
  :contained by: `vim.dvs.TrafficRule <vim/dvs/TrafficRule.rst>`_

  :type: `vim.dvs.TrafficRule.RuleDirectionType <vim/dvs/TrafficRule/RuleDirectionType.rst>`_

  :name: both

values:
--------

incomingPackets
   This specifies that the network rule has to be applied only for incoming packets.

both
   This specifies that the network rule has to be applied only for both incoming and outgoing packets.

outgoingPackets
   This specifies that the network rule has to be applied only for outgoing packets.
