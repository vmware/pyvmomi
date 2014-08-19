
vim.host.SnmpSystem.SnmpConfigSpec.Destination
==============================================
  Defines a receiver for SNMP Notifications
:extends: vmodl.DynamicData_

Attributes:
    hostName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A system listening for SNMP notifications. These must be a IPv4 unicast address or resolvable dns name.
    port (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       UDP port to Notification receiver is listening on. udp/162 is the reserved port
    community (`str <https://docs.python.org/2/library/stdtypes.html>`_):

