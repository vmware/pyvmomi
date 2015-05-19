.. _location: ../../../vim/vApp/CloneSpec/ResourceMap.rst#location

.. _vim.Datastore: ../../../vim/Datastore.rst

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _vim.ResourcePool: ../../../vim/ResourcePool.rst

.. _vim.ManagedEntity: ../../../vim/ManagedEntity.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.ResourceConfigSpec: ../../../vim/ResourceConfigSpec.rst


vim.vApp.CloneSpec.ResourceMap
==============================
  Maps source child entities to destination resource pools and resource settings. If a mapping is not specified, a child is copied as a direct child of the parent.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    source (`vim.ManagedEntity`_):

       Source entity
    parent (`vim.ResourcePool`_, privilege: Resource.AssignVAppToPool, optional):

       Resource pool to use for the cloned entity of source. This must specify a resource pool that is not part of the vApp. If this is specified, a linked child (as opposed to a direct child) is created for the vApp.
    resourceSpec (`vim.ResourceConfigSpec`_, optional):

       An optional resource configuration for the cloned entity of the source. If not specified, the same resource configuration as the source is used.
    location (`vim.Datastore`_, privilege: Datastore.AllocateSpace, optional):

       A client can optionally specify a datastore in the resource map to override the default datastore location set in `location`_ field. This enables cloning to different compute resources that do not have shared datastores.
