# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

from pyVmomi.vim.cluster import VsanVumSystemConfig

class VsanVumSystem(ManagedObject):
   def GetVsanVumConfig(self) -> VsanVumSystemConfig: ...
   def FetchIsoDepotCookie(self, username: str, password: str) -> NoReturn: ...
   def UpdateHostFirmware(self, host: HostSystem) -> Task: ...
   def UploadReleaseDb(self, db: str) -> NoReturn: ...
