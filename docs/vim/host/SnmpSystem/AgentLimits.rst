
vim.host.SnmpSystem.AgentLimits
===============================
  
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    maxReadOnlyCommunities (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       number of allowed communities
    maxTrapDestinations (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       number of allowed destinations for notifications
    maxCommunityLength (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Max length of community
    maxBufferSize (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       SNMP input buffer size
    capability (`vim.host.SnmpSystem.AgentLimits.Capability <vim/host/SnmpSystem/AgentLimits/Capability.rst>`_):

       Supported Capability for this agent
