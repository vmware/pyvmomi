.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _beacon: ../../../vim/host/VirtualSwitch/BondBridge.rst#beacon

.. _checkSpeed: ../../../vim/host/NetworkPolicy/NicFailureCriteria.rst#checkSpeed

.. _checkDuplex: ../../../vim/host/NetworkPolicy/NicFailureCriteria.rst#checkDuplex

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _checkErrorPercent: ../../../vim/host/NetworkPolicy/NicFailureCriteria.rst#checkErrorPercent

.. _HostVirtualSwitchBeaconConfig: ../../../vim/host/VirtualSwitch/BeaconConfig.rst


vim.host.NetworkPolicy.NicFailureCriteria
=========================================
  This data object type describes the network adapter failover detection algorithm for a network adapter team.
:extends: vmodl.DynamicData_

Attributes:
    checkSpeed (`str`_, optional):

       To use link speed as the criteria,checkSpeedmust be one of the following values:
        * 
        * exact
        * : Use exact speed to detect link failure.
        * speed
        * is the configured exact speed in megabits per second.
        * 
        * minimum
        * : Use minimum speed to detect failure.
        * speed
        * is the configured minimum speed in megabits per second.
        * 
        * empty string
        * : Do not use link speed to detect failure.
        * speed
        * is unused in this case.
        * 
    speed (`int`_, optional):

       see vim.host.NetworkPolicy.NicFailureCriteria#checkSpeedSee `checkSpeed`_ 
    checkDuplex (`bool`_, optional):

       The flag to indicate whether or not to use the link duplex reported by the driver as link selection criteria.IfcheckDuplexis true, then fullDuplex is the configured duplex mode. The link is considered bad if the link duplex reported by driver is not the same as fullDuplex.IfcheckDuplexis false, then fullDuplex is unused, and link duplexity is not used as a detection method.
    fullDuplex (`bool`_, optional):

       see vim.host.NetworkPolicy.NicFailureCriteria#checkDuplexSee `checkDuplex`_ 
    checkErrorPercent (`bool`_, optional):

       The flag to indicate whether or not to use link error percentage to detect failure.IfcheckErrorPercentis true, then percentage is the configured error percentage that is tolerated. The link is considered bad if error rate exceeds percentage.IfcheckErrorPercentis false, percentage is unused, and error percentage is not used as a detection method.
    percentage (`int`_, optional):

       see vim.host.NetworkPolicy.NicFailureCriteria#checkErrorPercentSee `checkErrorPercent`_ 
    checkBeacon (`bool`_, optional):

       The flag to indicate whether or not to enable this property to enable beacon probing as a method to validate the link status of a physical network adapter.checkBeaconcan be enabled only if the VirtualSwitch has been configured to use the beacon. Attempting to setcheckBeaconon a PortGroup or VirtualSwitch that does not have beacon probing configured for the applicable VirtualSwitch results in an error.See `beacon`_ See `HostVirtualSwitchBeaconConfig`_ 
