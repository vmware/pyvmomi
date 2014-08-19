
vim.dvs.VmwareDistributedVirtualSwitch.FailureCriteria
======================================================
  This data object type describes the network adapter failover detection algorithm for a network adapter team.
:extends: vim.InheritablePolicy_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    checkSpeed (`vim.StringPolicy <vim/StringPolicy.rst>`_, optional):

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
    speed (`vim.IntPolicy <vim/IntPolicy.rst>`_, optional):

       See `checkSpeed <vim/dvs/VmwareDistributedVirtualSwitch/FailureCriteria.rst#checkSpeed>`_ 
    checkDuplex (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       The flag to indicate whether or not to use the link duplex reported by the driver as link selection criteria.IfcheckDuplexis true, then fullDuplex is the configured duplex mode. The link is considered bad if the link duplex reported by driver is not the same as fullDuplex.IfcheckDuplexis false, then fullDuplex is unused, and link duplexity is not used as a detection method.
    fullDuplex (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       See `checkDuplex <vim/dvs/VmwareDistributedVirtualSwitch/FailureCriteria.rst#checkDuplex>`_ 
    checkErrorPercent (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       The flag to indicate whether or not to use link error percentage to detect failure.IfcheckErrorPercentis true, then percentage is the configured error percentage that is tolerated. The link is considered bad if error rate exceeds percentage.IfcheckErrorPercentis false, percentage is unused, and error percentage is not used as a detection method.
    percentage (`vim.IntPolicy <vim/IntPolicy.rst>`_, optional):

       See `checkErrorPercent <vim/dvs/VmwareDistributedVirtualSwitch/FailureCriteria.rst#checkErrorPercent>`_ 
    checkBeacon (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       The flag to indicate whether or not to enable this property to enable beacon probing as a method to validate the link status of a physical network adapter.checkBeaconcan be enabled only if the VirtualSwitch has been configured to use the beacon. Attempting to setcheckBeaconon a PortGroup or VirtualSwitch that does not have beacon probing configured for the applicable VirtualSwitch results in an error.
