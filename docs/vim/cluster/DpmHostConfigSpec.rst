
vim.cluster.DpmHostConfigSpec
=============================
  The `ClusterDpmHostConfigSpec <vim/cluster/DpmHostConfigSpec.rst>`_ data object provides information that the Server uses to update the DPM configuration for a single host (identified by the `key <vim/cluster/DpmHostConfigInfo.rst#key>`_ property). The host DPM configuration overrides the cluster default DPM setting ( `ClusterConfigSpecEx <vim/cluster/ConfigSpecEx.rst>`_ . `dpmConfig <vim/cluster/ConfigSpecEx.rst#dpmConfig>`_ ).The vSphere API defines three update operations ( `ArrayUpdateSpec <vim/option/ArrayUpdateSpec.rst>`_ . `operation <vim/option/ArrayUpdateSpec.rst#operation>`_ ).
   * add: Define DPM behavior for a host. If the cluster configuration already includes a DPM behavior override for the specified host, this operation removes the existing override and adds the new one. The new DPM override will use the cluster default value if you do not specify the behavior property (
   * `defaultDpmBehavior <vim/cluster/DpmConfigInfo.rst#defaultDpmBehavior>`_
   * ).
   * edit: Perform an incremental update to an existing DPM configuration entry for a host. The reconfigure method changes only the properties that you set in the data object. The entry must exist in the
   * `ClusterConfigSpecEx <vim/cluster/ConfigSpecEx.rst>`_
   * .
   * `dpmHostConfigSpec <vim/cluster/ConfigSpecEx.rst#dpmHostConfigSpec>`_
   * array.
   * remove: Remove the DPM override for the specified host. To identify the host to delete, use the
   * `removeKey <vim/option/ArrayUpdateSpec.rst#removeKey>`_
   * property to specify the
   * `key <vim/cluster/DpmHostConfigInfo.rst#key>`_
   * in the host override.Use the `ReconfigureComputeResource_Task <vim/ComputeResource.rst#reconfigureEx>`_ method to update the DPM configuration. If you set the modify parameter to true, you can use any of the three operations (add, edit, or remove). If you set the modify parameter to false, you can use only the add operation.
:extends: vim.option.ArrayUpdateSpec_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    info (`vim.cluster.DpmHostConfigInfo <vim/cluster/DpmHostConfigInfo.rst>`_, optional):

