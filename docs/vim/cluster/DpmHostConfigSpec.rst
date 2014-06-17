.. _removeKey: ../../vim/option/ArrayUpdateSpec.rst#removeKey

.. _dpmConfig: ../../vim/cluster/ConfigSpecEx.rst#dpmConfig

.. _operation: ../../vim/option/ArrayUpdateSpec.rst#operation

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _ArrayUpdateSpec: ../../vim/option/ArrayUpdateSpec.rst

.. _dpmHostConfigSpec: ../../vim/cluster/ConfigSpecEx.rst#dpmHostConfigSpec

.. _defaultDpmBehavior: ../../vim/cluster/DpmConfigInfo.rst#defaultDpmBehavior

.. _ClusterConfigSpecEx: ../../vim/cluster/ConfigSpecEx.rst

.. _ClusterDpmHostConfigSpec: ../../vim/cluster/DpmHostConfigSpec.rst

.. _vim.option.ArrayUpdateSpec: ../../vim/option/ArrayUpdateSpec.rst

.. _vim.cluster.DpmHostConfigInfo: ../../vim/cluster/DpmHostConfigInfo.rst

.. _ReconfigureComputeResource_Task: ../../vim/ComputeResource.rst#reconfigureEx


vim.cluster.DpmHostConfigSpec
=============================
  The `ClusterDpmHostConfigSpec`_ data object provides information that the Server uses to update the DPM configuration for a single host (identified by the `key`_ property). The host DPM configuration overrides the cluster default DPM setting ( `ClusterConfigSpecEx`_ . `dpmConfig`_ ).The vSphere API defines three update operations ( `ArrayUpdateSpec`_ . `operation`_ ).
   * add: Define DPM behavior for a host. If the cluster configuration already includes a DPM behavior override for the specified host, this operation removes the existing override and adds the new one. The new DPM override will use the cluster default value if you do not specify the behavior property (
   * `defaultDpmBehavior`_
   * ).
   * edit: Perform an incremental update to an existing DPM configuration entry for a host. The reconfigure method changes only the properties that you set in the data object. The entry must exist in the
   * `ClusterConfigSpecEx`_
   * .
   * `dpmHostConfigSpec`_
   * array.
   * remove: Remove the DPM override for the specified host. To identify the host to delete, use the
   * `removeKey`_
   * property to specify the
   * `key`_
   * in the host override.Use the `ReconfigureComputeResource_Task`_ method to update the DPM configuration. If you set the modify parameter to true, you can use any of the three operations (add, edit, or remove). If you set the modify parameter to false, you can use only the add operation.
:extends: vim.option.ArrayUpdateSpec_
:since: `VI API 2.5`_

Attributes:
    info (`vim.cluster.DpmHostConfigInfo`_, optional):

