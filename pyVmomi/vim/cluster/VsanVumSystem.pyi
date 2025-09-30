# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.Task import Task

from pyVmomi.vim.cluster.VsanVumSystemConfig import VsanVumSystemConfig

class VsanVumSystem(ManagedObject):
   def GetVsanVumConfig(self) -> VsanVumSystemConfig: ...
   def FetchIsoDepotCookie(self, username: str, password: str) -> None: ...
   def UpdateHostFirmware(self, host: HostSystem) -> Task: ...
   def UploadReleaseDb(self, db: str) -> None: ...
