.. _int: https://docs.python.org/2/library/stdtypes.html

.. _checkBeacon: ../../../vim/host/NetworkPolicy/NicFailureCriteria.rst#checkBeacon

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.VirtualSwitch.BeaconConfig
===================================
  This data object type describes the configuration of the beacon to probe connectivity of physical network adapters. A beacon is sent out of one network adapter and should arrive on another network adapter in the team. The successful roundtrip indicates that the network adapters are working.Define this data object to enable beacon probing as a method to validate the link status of a physical network adapter. Beacon probing must be configured in order to use the beacon status as a criteria to determine if a physical network adapter failed.See `checkBeacon`_ 
:extends: vmodl.DynamicData_

Attributes:
    interval (`int`_):

       Determines how often, in seconds, a beacon should be sent.
