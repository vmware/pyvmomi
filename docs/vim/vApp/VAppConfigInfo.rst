.. _str: https://docs.python.org/2/library/stdtypes.html

.. _managedBy: ../../vim/vApp/VAppConfigSpec.rst#managedBy

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.ext.ManagedByInfo: ../../vim/ext/ManagedByInfo.rst

.. _vim.vApp.VmConfigInfo: ../../vim/vApp/VmConfigInfo.rst

.. _vim.vApp.EntityConfigInfo: ../../vim/vApp/EntityConfigInfo.rst


vim.vApp.VAppConfigInfo
=======================
  Configuration of a vApp container.
:extends: vim.vApp.VmConfigInfo_
:since: `vSphere API 4.0`_

Attributes:
    entityConfig ([`vim.vApp.EntityConfigInfo`_], optional):

       Configuration of sub-entities (virtual machine or vApp).
    annotation (`str`_):

       Description for the vApp.
    instanceUuid (`str`_, optional):

       vCenter-specific 128-bit UUID of a vApp, represented as a hexademical string. This identifier is used by vCenter to uniquely identify all vApp instances.
    managedBy (`vim.ext.ManagedByInfo`_, optional):

       Specifies that this vApp is managed by a VC Extension. See the `managedBy`_ property in the VAppConfigSpec for more details.
