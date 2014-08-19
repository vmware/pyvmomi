
vim.vApp.VAppConfigInfo
=======================
  Configuration of a vApp container.
:extends: vim.vApp.VmConfigInfo_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    entityConfig ([`vim.vApp.EntityConfigInfo <vim/vApp/EntityConfigInfo.rst>`_], optional):

       Configuration of sub-entities (virtual machine or vApp).
    annotation (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Description for the vApp.
    instanceUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       vCenter-specific 128-bit UUID of a vApp, represented as a hexademical string. This identifier is used by vCenter to uniquely identify all vApp instances.
    managedBy (`vim.ext.ManagedByInfo <vim/ext/ManagedByInfo.rst>`_, optional):

       Specifies that this vApp is managed by a VC Extension. See the `managedBy <vim/vApp/VAppConfigSpec.rst#managedBy>`_ property in the VAppConfigSpec for more details.
