
vim.DistributedVirtualSwitch.Capability
=======================================
  The `DVSCapability <vim/DistributedVirtualSwitch/Capability.rst>`_ data object describes the distributed virtual switch features and indicates the level of configuration that is allowed.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    dvsOperationSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether this switch allows vCenter users to modify the switch configuration at the switch level, except for host member, policy, and scope operations.
    dvPortGroupOperationSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether this switch allows vCenter users to modify the switch configuration at the portgroup level, except for host member, policy, and scope operations.
    dvPortOperationSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether this switch allows vCenter users to modify the switch configuration at the port level, except for host member, policy, and scope operations.
    compatibleHostComponentProductInfo ([`vim.dvs.HostProductSpec <vim/dvs/HostProductSpec.rst>`_], optional):

       List of host component product information that is compatible with the current switch implementation.
    featuresSupported (`vim.DistributedVirtualSwitch.FeatureCapability <vim/DistributedVirtualSwitch/FeatureCapability.rst>`_, optional):

       Indicators for which version-specific distributed virtual switch features are available on this switch.This information is read-only, with the following exception. For a third-party distributed switch implementation, you can set the property `DVSFeatureCapability <vim/DistributedVirtualSwitch/FeatureCapability.rst>`_ . `vmDirectPathGen2Supported <vim/DistributedVirtualSwitch/FeatureCapability.rst#vmDirectPathGen2Supported>`_ during switch creation or when you call the `UpdateDvsCapability <vim/DistributedVirtualSwitch.rst#updateCapability>`_ method.
