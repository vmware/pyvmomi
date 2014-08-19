
vim.dvs.DistributedVirtualSwitchManager.HostContainer
=====================================================
  Check host compatibility for all hosts in the container. If the recursive flag is true, then check hosts at all levels within this container, otherwise check only at the container level. In case of container being a `Datacenter <vim/Datacenter.rst>`_ , the recursive flag is applied to its HostFolder.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    container (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):

       Check compatibility of hosts in this container. The supported container types are Datacenter, Folder, and ComputeResource.
    recursive (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       If true, include hosts of all levels in the hierarchy with container as root of the tree. In case of container being a `Datacenter <vim/Datacenter.rst>`_ , the recursive flag is applied to its HostFolder.
