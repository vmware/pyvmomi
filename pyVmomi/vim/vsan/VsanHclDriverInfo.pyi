# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import VsanDownloadItem

class VsanHclDriverInfo(DynamicData):
   driverVersion: Optional[str] = None
   driverLink: Optional[VsanDownloadItem] = None
   fwVersion: Optional[str] = None
   fwLinks: list[VsanDownloadItem] = []
   toolsLinks: list[VsanDownloadItem] = []
   eula: Optional[str] = None
   driverType: Optional[str] = None
   driverName: Optional[str] = None
   diskModes: list[str] = []
   supportedFeatures: list[str] = []
