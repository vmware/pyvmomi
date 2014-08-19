
vim.host.PortGroup.Config
=========================
  This describes the port group configuration containing both the configurable properties on a port group and the associated virtual switch.
:extends: vmodl.DynamicData_

Attributes:
    changeOperation (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates the change operation to apply on this configuration specification.See `HostConfigChangeOperation <vim/host/ConfigChange/Operation.rst>`_ 
    spec (`vim.host.PortGroup.Specification <vim/host/PortGroup/Specification.rst>`_, optional):

       The specification of the port group.
