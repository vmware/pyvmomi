.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst


vim.host.SnmpSystem.SnmpConfigSpec.Destination
==============================================
  Defines a receiver for SNMP Notifications
:extends: vmodl.DynamicData_

Attributes:
    hostName (`str`_):

       A system listening for SNMP notifications. These must be a IPv4 unicast address or resolvable dns name.
    port (`int`_):

       UDP port to Notification receiver is listening on. udp/162 is the reserved port
    community (`str`_):

