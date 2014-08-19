
vim.OvfManager.ResourceMap
==========================
  Maps source child entities to destination resource pools and resource settings. If a mapping is not specified, a child is copied as a direct child of the parent.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_
**deprecated**


Attributes:
    source (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Identifies a source VirtualSystem or VirtualSystemCollection in an OVF descriptor. The source cannot be the root VirtualSystem or VirtualSystemCollection of the OVF. This is a path created by concatenating the OVF ids for each entity, e.g., "vm1", "WebTier/vm2", etc.
    parent (`vim.ResourcePool <vim/ResourcePool.rst>`_, optional):

       The parent resource pool to use for the entity. This must specify a resource pool that is not part of the vApp. If this is specified, a linked child (as opposed to a direct child) is created for the vApp.
    resourceSpec (`vim.ResourceConfigSpec <vim/ResourceConfigSpec.rst>`_, optional):

       An optional resource configuration for the created entity. If not specified, the resource configuration given in the OVF descriptor is used.
    datastore (`vim.Datastore <vim/Datastore.rst>`_, privilege: Datastore.AllocateSpace, optional):

       A client can optionally specify a datastore location in the resource map to override the default datastore passed into `CreateImportSpec <vim/OvfManager.rst#createImportSpec>`_ field. This enables importing to different compute resources that do not have shared datastores.
