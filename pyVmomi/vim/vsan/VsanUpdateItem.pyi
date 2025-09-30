# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.VsanHclFirmwareUpdateSpec import VsanHclFirmwareUpdateSpec

from pyVmomi.vim.vsan.VsanDownloadItem import VsanDownloadItem

from pyVmomi.vim.vsan.VsanVibSpec import VsanVibSpec

class VsanUpdateItem(DynamicData):
   host: HostSystem
   type: str
   name: str
   version: str
   existingVersion: Optional[str] = None
   present: bool
   vibSpec: list[VsanVibSpec] = []
   vibType: Optional[str] = None
   firmwareSpec: Optional[VsanHclFirmwareUpdateSpec] = None
   downloadInfo: list[VsanDownloadItem] = []
   eula: Optional[str] = None
   adapter: Optional[str] = None
   key: Optional[str] = None
   impact: Optional[str] = None
   firmwareUnknown: Optional[bool] = None
