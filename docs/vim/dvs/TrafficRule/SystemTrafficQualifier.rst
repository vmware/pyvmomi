
vim.dvs.TrafficRule.SystemTrafficQualifier
==========================================
  This class defines the System Traffic Qualifier. Here the type of traffic will be used for classifying packets.
:extends: vim.dvs.TrafficRule.Qualifier_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    typeOfSystemTraffic (`vim.StringExpression <vim/StringExpression.rst>`_, optional):

       Type of system traffic. See `DistributedVirtualSwitchHostInfrastructureTrafficClass <vim/DistributedVirtualSwitch/HostInfrastructureTrafficClass.rst>`_ for valid values.
