# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import VsanCompliantFirmware

class VsanHclDeviceConstraint(DynamicData):
   pciId: str
   vcgLink: Optional[str] = None
   similarVcgLinks: list[str] = []
   compliantFirmwares: list[VsanCompliantFirmware] = []
   vcgId: Optional[int] = None
   model: Optional[str] = None
   partner: Optional[str] = None
   partNumber: Optional[str] = None
   release: Optional[str] = None
