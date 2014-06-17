.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _ipfixEnabled: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst#ipfixEnabled

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VMwareDVSPortSetting: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst


vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig
==================================================
  Configuration for IPFIX monitoring of distributed virtual switch traffic. IPFIX monitoring must be enabled to use this capability. See `VMwareDVSPortSetting`_ . `ipfixEnabled`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    collectorIpAddress (`str`_, optional):

       IP address for the ipfix collector, specified using IPv4 dot notation. This must be set before ipfix monitoring can be enabled for the switch, or for any portgroup or port of the switch.
    collectorPort (`int`_, optional):

       Port for the ipfix collector. This must be set before ipfix monitoring can be enabled for the switch, or for any portgroup or port of the switch. Legal value range is 0-65535.
    activeFlowTimeout (`int`_):

       The number of seconds after which "active" flows are forced to be exported to the collector. Legal value range is 60-3600. Default 60.
    idleFlowTimeout (`int`_):

       The number of seconds after which "idle" flows are forced to be exported to the collector. Legal value range is 10-600. Default 15.
    samplingRate (`int`_):

       The ratio of total number of packets to the number of packets analyzed. Set to 0 to disable sampling. Legal value range is 0-1000. Default 0.
    internalFlowsOnly (`bool`_):

       Whether to limit analysis to traffic that has both source and destination served by the same host. Default false.
