
vim.ResourceConfigSpec
======================
  This data object type is a specification for a set of resources allocated to a virtual machine or a resource pool.
:extends: vmodl.DynamicData_

Attributes:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_, optional):

       Reference to the entity with this resource specification: either a VirtualMachine or a ResourcePool.
    changeVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The changeVersion is a unique identifier for a given version of the configuration. Each change to the configuration will update this value. This is typically implemented as an ever increasing count or a time-stamp. However, a client should always treat this as an opaque string.If specified when updating the resource config., the changes will only be applied if the current changeVersion matches the specified changeVersion. This field can be used to guard against updates that has happened between the configInfo was read and until it is applied.
    lastModified (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Timestamp when the resources were last modified. This is ignored when the object is used to update a configuration.
    cpuAllocation (`vim.ResourceAllocationInfo <vim/ResourceAllocationInfo.rst>`_):

       Resource allocation for CPU.
    memoryAllocation (`vim.ResourceAllocationInfo <vim/ResourceAllocationInfo.rst>`_):

       Resource allocation for memory.
