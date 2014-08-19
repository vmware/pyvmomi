
vim.host.VirtualSwitch.Config
=============================
  This data object type describes the VirtualSwitch configuration containing both the configurable properties on a VirtualSwitch and identification information.
:extends: vmodl.DynamicData_

Attributes:
    changeOperation (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       This property indicates the change operation to apply on this configuration specification.See `HostConfigChangeOperation <vim/host/ConfigChange/Operation.rst>`_ 
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the virtual switch. Maximum length is 32 characters.
    spec (`vim.host.VirtualSwitch.Specification <vim/host/VirtualSwitch/Specification.rst>`_, optional):

       The specification of the VirtualSwitch.
