
vim.VirtualApp.LinkInfo
=======================
  Linked child information.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_
**deprecated**


Attributes:
    key (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):

       The key contains a reference to the entity that is linked to this vApp
    destroyWithParent (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether the entity should be removed, when this vApp is removed
