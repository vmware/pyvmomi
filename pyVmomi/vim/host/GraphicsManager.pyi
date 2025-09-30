# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ExtensibleManagedObject import ExtensibleManagedObject

from pyVmomi.vim.host.GraphicsConfig import GraphicsConfig

from pyVmomi.vim.host.GraphicsInfo import GraphicsInfo

from pyVmomi.vim.host.SharedGpuCapabilities import SharedGpuCapabilities

from pyVmomi.vim.vm.VgpuDeviceInfo import VgpuDeviceInfo

from pyVmomi.vim.vm.VgpuProfileInfo import VgpuProfileInfo

class GraphicsManager(ExtensibleManagedObject):
   @property
   def graphicsInfo(self) -> list[GraphicsInfo]: ...
   @property
   def graphicsConfig(self) -> Optional[GraphicsConfig]: ...
   @property
   def sharedPassthruGpuTypes(self) -> list[str]: ...
   @property
   def sharedGpuCapabilities(self) -> list[SharedGpuCapabilities]: ...

   def RetrieveVgpuDeviceInfo(self) -> list[VgpuDeviceInfo]: ...
   def RetrieveVgpuProfileInfo(self) -> list[VgpuProfileInfo]: ...
   def Refresh(self) -> None: ...
   def IsSharedGraphicsActive(self) -> bool: ...
   def UpdateGraphicsConfig(self, config: GraphicsConfig) -> None: ...
