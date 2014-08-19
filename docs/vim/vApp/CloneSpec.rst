
vim.vApp.CloneSpec
==================
  Specification for a vApp cloning operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    location (`vim.Datastore <vim/Datastore.rst>`_, privilege: Datastore.AllocateSpace):

       Location where the destination vApp must be stored
    host (`vim.HostSystem <vim/HostSystem.rst>`_, privilege: VApp.Create, optional):

       The target host for the virtual machines. This is often not a required parameter. If not specified, the behavior is as follows:
        * If the target pool represents a stand-alone host, that host is used.
        * If the target pool represents a DRS-enabled cluster, a host selected by DRS is used.
        * If the target pool represents a cluster without DRS enabled or a DRS-enabled cluster in manual mode, an InvalidArgument exception is thrown.
        * 
    resourceSpec (`vim.ResourceConfigSpec <vim/ResourceConfigSpec.rst>`_, optional):

       The resource configuration for the vApp.
    vmFolder (`vim.Folder <vim/Folder.rst>`_, privilege: VApp.Create, optional):

       The VM Folder to associate the vApp with
    networkMapping ([`vim.vApp.CloneSpec.NetworkMappingPair <vim/vApp/CloneSpec/NetworkMappingPair.rst>`_], optional):

       Network mappings. See NetworkMappingPair.
    property ([`vim.KeyValue <vim/KeyValue.rst>`_], optional):

       A set of property values to override.
    resourceMapping ([`vim.vApp.CloneSpec.ResourceMap <vim/vApp/CloneSpec/ResourceMap.rst>`_], optional):

       The resource configuration for the cloned vApp.
    provisioning (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specify how the VMs in the vApp should be provisioned.
