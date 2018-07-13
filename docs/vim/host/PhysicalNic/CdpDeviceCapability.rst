.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _PhysicalNicCdpInfo: ../../../vim/host/PhysicalNic/CdpInfo.rst


vim.host.PhysicalNic.CdpDeviceCapability
========================================
  The capability of the CDP-awarded device that connects to a Physical NIC. `PhysicalNicCdpInfo`_
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    router (`bool`_):

       The CDP-awarded device has the capability of a routing for at least one network layer protocol
    transparentBridge (`bool`_):

       The CDP-awarded device has the capability of transparent bridging
    sourceRouteBridge (`bool`_):

       The CDP-awarded device has the capability of source-route bridging
    networkSwitch (`bool`_):

       The CDP-awarded device has the capability of switching. The difference between this capability and transparentBridge is that a switch does not run the Spanning-Tree Protocol. This device is assumed to be deployed in a physical loop-free topology.
    host (`bool`_):

       The CDP-awarded device has the capability of a host, which Sends and receives packets for at least one network layer protocol.
    igmpEnabled (`bool`_):

       The CDP-awarded device is IGMP-enabled, which does not forward IGMP Report packets on nonrouter ports.
    repeater (`bool`_):

       The CDP-awarded device has the capability of a repeater
