
vim.dvs.VmwareDistributedVirtualSwitch.FeatureCapability
========================================================
  Indicators of support for version-specific DVS features that are only available on a VMware-class switch.
:extends: vim.DistributedVirtualSwitch.FeatureCapability_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    vspanSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether vspan(DVMirror) is supported on the vSphere Distributed Switch. Distributed Port Mirroring is supported in vSphere Distributed Switch Version 5.0 or later.
    lldpSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether LLDP(Link Layer Discovery Protocol) is supported on the vSphere Distributed Switch. LLDP is supported in vSphere Distributed Switch Version 5.0 or later.
    ipfixSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether IPFIX(NetFlow) is supported on the vSphere Distributed Switch. IPFIX is supported in vSphere Distributed Switch Version 5.0 or later.
    vspanCapability (`vim.dvs.VmwareDistributedVirtualSwitch.VspanFeatureCapability <vim/dvs/VmwareDistributedVirtualSwitch/VspanFeatureCapability.rst>`_, optional):

       The support for version-specific Distributed Port Mirroring sessions.
    lacpCapability (`vim.dvs.VmwareDistributedVirtualSwitch.LacpFeatureCapability <vim/dvs/VmwareDistributedVirtualSwitch/LacpFeatureCapability.rst>`_, optional):

       The support for version-specific Link Aggregation Control Protocol.
