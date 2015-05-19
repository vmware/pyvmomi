.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _enabled: ../../../vim/vsan/cluster/ConfigInfo.rst#enabled

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VsanClusterConfigInfo: ../../../vim/vsan/cluster/ConfigInfo.rst

.. _ReconfigureComputeResource_Task: ../../../vim/ComputeResource.rst#reconfigureEx

.. _vim.vsan.cluster.ConfigInfo.HostDefaultInfo: ../../../vim/vsan/cluster/ConfigInfo/HostDefaultInfo.rst


vim.vsan.cluster.ConfigInfo
===========================
  The `VsanClusterConfigInfo`_ data object contains configuration data for the VSAN service in a cluster. This data object is used both for specifying cluster-wide settings when updating the VSAN service, and as an output datatype when retrieving current cluster-wide VSAN service settings.See `ReconfigureComputeResource_Task`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    enabled (`bool`_, optional):

       Whether the VSAN service is enabled for the cluster.
    defaultConfig (`vim.vsan.cluster.ConfigInfo.HostDefaultInfo`_, optional):

       Default VSAN settings to use for hosts admitted to the cluster when the VSAN service is enabled. If omitted, values will default as though the fields in the HostDefaultInfo have been omitted.See `enabled`_ See HostDefaultInfo
