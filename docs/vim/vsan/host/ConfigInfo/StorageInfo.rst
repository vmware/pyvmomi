
vim.vsan.host.ConfigInfo.StorageInfo
====================================
  Host-local VSAN storage configuration. This data object is used both for specifying and retrieving storage configuration for a host participating in the VSAN service.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    autoClaimStorage (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether the VSAN service is configured to automatically claim local unused storage on this host. When set, the VSAN service will automatically format and use local disks. Side effects from any disk consumption will be reflected in `diskMapping <vim/vsan/host/ConfigInfo/StorageInfo.rst#diskMapping>`_ . If this argument is specified as a host-level configuration input at the VC-level (see `vsanHostConfig <vim/cluster/ConfigInfoEx.rst#vsanHostConfig>`_ ), it will override that of any cluster-level default value.See `diskMapping <vim/vsan/host/ConfigInfo/StorageInfo.rst#diskMapping>`_ See `vsanHostConfig <vim/cluster/ConfigInfoEx.rst#vsanHostConfig>`_ See `defaultConfig <vim/vsan/cluster/ConfigInfo.rst#defaultConfig>`_ 
    diskMapping ([`vim.vsan.host.DiskMapping <vim/vsan/host/DiskMapping.rst>`_], optional):

       List of `VsanHostDiskMapping <vim/vsan/host/DiskMapping.rst>`_ entries in use by the VSAN service. DiskMappings to be used by the VSAN service may be manually specified using vim.host.VsanSystem#initializeDisks(DiskMapping[]).See vim.host.VsanSystem#initializeDisks(DiskMapping[])
