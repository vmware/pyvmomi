# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vim.host import GraphicsConfig
from pyVmomi.vim.host import GraphicsInfo
from pyVmomi.vim.host import SharedGpuCapabilities

from pyVmomi.vim.vm import VgpuDeviceInfo
from pyVmomi.vim.vm import VgpuProfileInfo

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
   def Refresh(self) -> NoReturn: ...
   def IsSharedGraphicsActive(self) -> bool: ...
   def UpdateGraphicsConfig(self, config: GraphicsConfig) -> NoReturn: ...
