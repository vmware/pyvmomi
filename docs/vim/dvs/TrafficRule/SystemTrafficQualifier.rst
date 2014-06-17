.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vim.StringExpression: ../../../vim/StringExpression.rst

.. _vim.dvs.TrafficRule.Qualifier: ../../../vim/dvs/TrafficRule/Qualifier.rst

.. _DistributedVirtualSwitchHostInfrastructureTrafficClass: ../../../vim/DistributedVirtualSwitch/HostInfrastructureTrafficClass.rst


vim.dvs.TrafficRule.SystemTrafficQualifier
==========================================
  This class defines the System Traffic Qualifier. Here the type of traffic will be used for classifying packets.
:extends: vim.dvs.TrafficRule.Qualifier_
:since: `vSphere API 5.5`_

Attributes:
    typeOfSystemTraffic (`vim.StringExpression`_, optional):

       Type of system traffic. See `DistributedVirtualSwitchHostInfrastructureTrafficClass`_ for valid values.
