
vim.vsan.cluster.ConfigInfo
===========================
  The `VsanClusterConfigInfo <vim/vsan/cluster/ConfigInfo.rst>`_ data object contains configuration data for the VSAN service in a cluster. This data object is used both for specifying cluster-wide settings when updating the VSAN service, and as an output datatype when retrieving current cluster-wide VSAN service settings.See `ReconfigureComputeResource_Task <vim/ComputeResource.rst#reconfigureEx>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether the VSAN service is enabled for the cluster.
    defaultConfig (`vim.vsan.cluster.ConfigInfo.HostDefaultInfo <vim/vsan/cluster/ConfigInfo/HostDefaultInfo.rst>`_, optional):

       Default VSAN settings to use for hosts admitted to the cluster when the VSAN service is enabled. If omitted, values will default as though the fields in the HostDefaultInfo have been omitted.See `enabled <vim/vsan/cluster/ConfigInfo.rst#enabled>`_ See HostDefaultInfo
