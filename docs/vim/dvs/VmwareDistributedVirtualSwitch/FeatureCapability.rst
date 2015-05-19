.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _vim.DistributedVirtualSwitch.FeatureCapability: ../../../vim/DistributedVirtualSwitch/FeatureCapability.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.LacpFeatureCapability: ../../../vim/dvs/VmwareDistributedVirtualSwitch/LacpFeatureCapability.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.VspanFeatureCapability: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VspanFeatureCapability.rst


vim.dvs.VmwareDistributedVirtualSwitch.FeatureCapability
========================================================
  Indicators of support for version-specific DVS features that are only available on a VMware-class switch.
:extends: vim.DistributedVirtualSwitch.FeatureCapability_
:since: `vSphere API 4.1`_

Attributes:
    vspanSupported (`bool`_, optional):

       Flag to indicate whether vspan(DVMirror) is supported on the vSphere Distributed Switch. Distributed Port Mirroring is supported in vSphere Distributed Switch Version 5.0 or later.
    lldpSupported (`bool`_, optional):

       Flag to indicate whether LLDP(Link Layer Discovery Protocol) is supported on the vSphere Distributed Switch. LLDP is supported in vSphere Distributed Switch Version 5.0 or later.
    ipfixSupported (`bool`_, optional):

       Flag to indicate whether IPFIX(NetFlow) is supported on the vSphere Distributed Switch. IPFIX is supported in vSphere Distributed Switch Version 5.0 or later.
    vspanCapability (`vim.dvs.VmwareDistributedVirtualSwitch.VspanFeatureCapability`_, optional):

       The support for version-specific Distributed Port Mirroring sessions.
    lacpCapability (`vim.dvs.VmwareDistributedVirtualSwitch.LacpFeatureCapability`_, optional):

       The support for version-specific Link Aggregation Control Protocol.
