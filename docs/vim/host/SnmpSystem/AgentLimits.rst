.. _int: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.SnmpSystem.AgentLimits.Capability: ../../../vim/host/SnmpSystem/AgentLimits/Capability.rst


vim.host.SnmpSystem.AgentLimits
===============================
  
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    maxReadOnlyCommunities (`int`_):

       number of allowed communities
    maxTrapDestinations (`int`_):

       number of allowed destinations for notifications
    maxCommunityLength (`int`_):

       Max length of community
    maxBufferSize (`int`_):

       SNMP input buffer size
    capability (`vim.host.SnmpSystem.AgentLimits.Capability`_):

       Supported Capability for this agent
