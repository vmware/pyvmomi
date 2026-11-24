# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.vim
import pyVmomi.vmodl



class ExtendedProductInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object encapsulates extended product information for an extension.
   
   Attributes:
       companyUrl: URL to extension vendor.
       productUrl: URL to vendor's description of this extension.
       managementUrl: URL to management UI for this extension.
       self: The VirtualMachine or VirtualApp that is running this extension.
   """
   companyUrl: _typing.Optional[str] = None
   productUrl: _typing.Optional[str] = None
   managementUrl: _typing.Optional[str] = None
   self: _typing.Optional[pyVmomi.vim.ManagedEntity] = None


class ManagedByInfo(pyVmomi.vmodl.DynamicData):
   """
   The ManagedByInfo data object contains information about the extension
   responsible for the life-cycle of the entity.
   
   Attributes:
       extensionKey: Key of the extension managing the entity.
       type: Managed entity type, as defined by the extension managing the entity.
           
           An extension can manage different types of entities - different kinds
           of virtual machines, vApps, etc. - and this property is used to find
           the corresponding `pyVmomi.vim.ext.ManagedEntityInfo`
           entry from the extension.
   """
   extensionKey: str
   type: str


class ManagedEntityInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object contains information about entities managed by this
   extension.
   
   The data can be used by clients to show extra information
   about managed virtual machines or vApps, such as a custom icon and a
   description of the entity.
   
   Attributes:
       type: Managed entity type, as defined by the extension.
           
           This matches the
           `pyVmomi.vim.ext.ManagedByInfo.type` field in the configuration
           about a virtual machine or vApp.
       smallIconUrl: The URL to a 16x16 pixel icon in PNG format for entities of this
           type managed by this extension.
           
           The design of the icon should
           allow for the possibility of it being badged with the power state
           of the entity by the vSphere client. If you do not provide this
           icon, the icon at
           `pyVmomi.vim.ext.ManagedEntityInfo.iconUrl`, if found, is
           scaled down to 16x16 pixels.
       iconUrl: The URL to an icon in PNG format that is no larger than 256x256
           pixels.
           
           This icon will be scaled to 16x16, 32x32, 64x64, and
           128x128 if needed. The icon is shown for all entities of this type
           managed by this extension.
       description: Description of this managed entity type.
           
           This is typically displayed
           by clients, and should provide users with information about the
           function of entities of this type.
   """
   type: str
   smallIconUrl: _typing.Optional[str] = None
   iconUrl: _typing.Optional[str] = None
   description: _typing.Optional[str] = None


class SolutionManagerInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object encapsulates the Solution Manager configuration for
   this extension.
   
   Attributes:
       tab: List of tabs that must be shown in the Solution Manager for this extension.
           
           Tabs are shown ordered by their position in this array.
       smallIconUrl: URL for an icon for this extension.
           
           The icon will be shown in the Solution
           Manager for this extension. The icon must be 16x16, and should be in PNG
           format.
   """
   class TabInfo(pyVmomi.vmodl.DynamicData):
      """
      Deprecated: As of vSphere API 5.1.This data object contains information about a tab to show in the
      Solution Manager for this extension.
      
      Attributes:
          label: The name of the tab.
          url: The URL for the webpage to show in the tab.
              
              Extra parameters will be added
              to this URL when vSphere Client loads it. See the \"Customizing the vSphere
              Client\" technical note for more information.
      """
      label: str
      url: str

   tab: list[SolutionManagerInfo.TabInfo] = []
   smallIconUrl: _typing.Optional[str] = None
