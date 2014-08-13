.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _DVSCapability: ../../vim/DistributedVirtualSwitch/Capability.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _UpdateDvsCapability: ../../vim/DistributedVirtualSwitch.rst#updateCapability

.. _DVSFeatureCapability: ../../vim/DistributedVirtualSwitch/FeatureCapability.rst

.. _vim.dvs.HostProductSpec: ../../vim/dvs/HostProductSpec.rst

.. _vmDirectPathGen2Supported: ../../vim/DistributedVirtualSwitch/FeatureCapability.rst#vmDirectPathGen2Supported

.. _vim.DistributedVirtualSwitch.FeatureCapability: ../../vim/DistributedVirtualSwitch/FeatureCapability.rst


vim.DistributedVirtualSwitch.Capability
=======================================
  The `DVSCapability`_ data object describes the distributed virtual switch features and indicates the level of configuration that is allowed.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    dvsOperationSupported (`bool`_, optional):

       Indicates whether this switch allows vCenter users to modify the switch configuration at the switch level, except for host member, policy, and scope operations.
    dvPortGroupOperationSupported (`bool`_, optional):

       Indicates whether this switch allows vCenter users to modify the switch configuration at the portgroup level, except for host member, policy, and scope operations.
    dvPortOperationSupported (`bool`_, optional):

       Indicates whether this switch allows vCenter users to modify the switch configuration at the port level, except for host member, policy, and scope operations.
    compatibleHostComponentProductInfo ([`vim.dvs.HostProductSpec`_], optional):

       List of host component product information that is compatible with the current switch implementation.
    featuresSupported (`vim.DistributedVirtualSwitch.FeatureCapability`_, optional):

       Indicators for which version-specific distributed virtual switch features are available on this switch.This information is read-only, with the following exception. For a third-party distributed switch implementation, you can set the property `DVSFeatureCapability`_ . `vmDirectPathGen2Supported`_ during switch creation or when you call the `UpdateDvsCapability`_ method.
