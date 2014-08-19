
vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig
==================================================
  Configuration for IPFIX monitoring of distributed virtual switch traffic. IPFIX monitoring must be enabled to use this capability. See `VMwareDVSPortSetting <vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst>`_ . `ipfixEnabled <vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst#ipfixEnabled>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    collectorIpAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       IP address for the ipfix collector, specified using IPv4 dot notation. This must be set before ipfix monitoring can be enabled for the switch, or for any portgroup or port of the switch.
    collectorPort (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Port for the ipfix collector. This must be set before ipfix monitoring can be enabled for the switch, or for any portgroup or port of the switch. Legal value range is 0-65535.
    activeFlowTimeout (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of seconds after which "active" flows are forced to be exported to the collector. Legal value range is 60-3600. Default 60.
    idleFlowTimeout (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of seconds after which "idle" flows are forced to be exported to the collector. Legal value range is 10-600. Default 15.
    samplingRate (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The ratio of total number of packets to the number of packets analyzed. Set to 0 to disable sampling. Legal value range is 0-1000. Default 0.
    internalFlowsOnly (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether to limit analysis to traffic that has both source and destination served by the same host. Default false.
