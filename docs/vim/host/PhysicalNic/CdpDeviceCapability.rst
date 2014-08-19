
vim.host.PhysicalNic.CdpDeviceCapability
========================================
  The capability of the CDP-awared device that connects to a Physical NIC. `PhysicalNicCdpInfo <vim/host/PhysicalNic/CdpInfo.rst>`_ 
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    router (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The CDP-awared device has the capability of a routing for at least one network layer protocol
    transparentBridge (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The CDP-awared device has the capability of transparent bridging
    sourceRouteBridge (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The CDP-awared device has the capability of source-route bridging
    networkSwitch (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The CDP-awared device has the capability of switching. The difference between this capability and transparentBridge is that a switch does not run the Spanning-Tree Protocol. This device is assumed to be deployed in a physical loop-free topology.
    host (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The CDP-awared device has the capability of a host, which Sends and receives packets for at least one network layer protocol.
    igmpEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The CDP-awared device is IGMP-enabled, which does not forward IGMP Report packets on nonrouter ports.
    repeater (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The CDP-awared device has the capability of a repeater
