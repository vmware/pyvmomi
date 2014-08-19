
vim.vsan.host.ConfigInfo
========================
  The `VsanHostConfigInfo <vim/vsan/host/ConfigInfo.rst>`_ data object contains host-specific settings for the VSAN service. This data object is used both for specifying settings for updating the VSAN service, and as an output datatype when retrieving current VSAN service settings.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether the VSAN service is currently enabled on this host.
    hostSystem (`vim.HostSystem <vim/HostSystem.rst>`_, optional):

       The `HostSystem <vim/HostSystem.rst>`_ for this host. This argument is required when this configuration is specified as an input to VC-level APIs. When this configuration is specified to a host-level direct API, this argument may be omitted.See `ReconfigureComputeResource_Task <vim/ComputeResource.rst#reconfigureEx>`_ See `UpdateVsan_Task <vim/host/VsanSystem.rst#update>`_ 
    clusterInfo (`vim.vsan.host.ConfigInfo.ClusterInfo <vim/vsan/host/ConfigInfo/ClusterInfo.rst>`_, optional):

       The VSAN service cluster configuration for this host.
    storageInfo (`vim.vsan.host.ConfigInfo.StorageInfo <vim/vsan/host/ConfigInfo/StorageInfo.rst>`_, optional):

       The VSAN storage configuration for this host. VSAN storage configuration settings are independent of the current value of `enabled <vim/vsan/host/ConfigInfo.rst#enabled>`_ .
    networkInfo (`vim.vsan.host.ConfigInfo.NetworkInfo <vim/vsan/host/ConfigInfo/NetworkInfo.rst>`_, optional):

       The VSAN network configuration for this host. VSAN network configuration settings are independent of the current value of `enabled <vim/vsan/host/ConfigInfo.rst#enabled>`_ .
