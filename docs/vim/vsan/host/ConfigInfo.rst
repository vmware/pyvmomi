.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _enabled: ../../../vim/vsan/host/ConfigInfo.rst#enabled

.. _HostSystem: ../../../vim/HostSystem.rst

.. _vim.HostSystem: ../../../vim/HostSystem.rst

.. _UpdateVsan_Task: ../../../vim/host/VsanSystem.rst#update

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VsanHostConfigInfo: ../../../vim/vsan/host/ConfigInfo.rst

.. _ReconfigureComputeResource_Task: ../../../vim/ComputeResource.rst#reconfigureEx

.. _vim.vsan.host.ConfigInfo.NetworkInfo: ../../../vim/vsan/host/ConfigInfo/NetworkInfo.rst

.. _vim.vsan.host.ConfigInfo.StorageInfo: ../../../vim/vsan/host/ConfigInfo/StorageInfo.rst

.. _vim.vsan.host.ConfigInfo.ClusterInfo: ../../../vim/vsan/host/ConfigInfo/ClusterInfo.rst


vim.vsan.host.ConfigInfo
========================
  The `VsanHostConfigInfo`_ data object contains host-specific settings for the VSAN service. This data object is used both for specifying settings for updating the VSAN service, and as an output datatype when retrieving current VSAN service settings.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    enabled (`bool`_, optional):

       Whether the VSAN service is currently enabled on this host.
    hostSystem (`vim.HostSystem`_, optional):

       The `HostSystem`_ for this host. This argument is required when this configuration is specified as an input to VC-level APIs. When this configuration is specified to a host-level direct API, this argument may be omitted.See `ReconfigureComputeResource_Task`_ See `UpdateVsan_Task`_ 
    clusterInfo (`vim.vsan.host.ConfigInfo.ClusterInfo`_, optional):

       The VSAN service cluster configuration for this host.
    storageInfo (`vim.vsan.host.ConfigInfo.StorageInfo`_, optional):

       The VSAN storage configuration for this host. VSAN storage configuration settings are independent of the current value of `enabled`_ .
    networkInfo (`vim.vsan.host.ConfigInfo.NetworkInfo`_, optional):

       The VSAN network configuration for this host. VSAN network configuration settings are independent of the current value of `enabled`_ .
