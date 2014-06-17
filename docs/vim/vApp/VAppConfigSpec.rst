.. _str: https://docs.python.org/2/library/stdtypes.html

.. _managedBy: ../../vim/ext/ManagedByInfo.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _managedEntityInfo: ../../vim/Extension.rst#managedEntityInfo

.. _vim.ext.ManagedByInfo: ../../vim/ext/ManagedByInfo.rst

.. _vim.vApp.VmConfigSpec: ../../vim/vApp/VmConfigSpec.rst

.. _vim.vApp.EntityConfigInfo: ../../vim/vApp/EntityConfigInfo.rst


vim.vApp.VAppConfigSpec
=======================
  Configuration of a vApp
:extends: vim.vApp.VmConfigSpec_
:since: `vSphere API 4.0`_

Attributes:
    entityConfig (`vim.vApp.EntityConfigInfo`_, optional):

       Configuration of sub-entities (virtual machine or vApp container).Reconfigure privilege: See EntityConfigInfo
    annotation (`str`_, optional):

       Description for the vApp.Reconfigure privilege: VApp.Rename.
    instanceUuid (`str`_, optional):

       vCenter-specific 128-bit UUID of a vApp, represented as a hexadecimal string. This identifier is used by vCenter to uniquely identify all vApp instances in the Virtual Infrastructure environment.Normally, this property is not set by a client, allowing the Virtual Infrastructure environment to assign or change it when VirtualCenter detects an identifier conflict between vApps.Reconfigure privilege: VApp.ApplicationConfig
    managedBy (`vim.ext.ManagedByInfo`_, optional):

       Specifies that this vApp is managed by a VC Extension.This information is primarily used in the Client to show a custom icon for managed vApps, and a description of the function of the vApp. If no extension can be found with the extension key in the `managedBy`_ object, or the type is not found in the `managedEntityInfo`_ list of the extension, the default vApp icon is used, and no description is shown.Reconfigure privilege: VApp.ApplicationConfig
