# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanHclFirmwareFile
from pyVmomi.vim.host import VsanHostFwComponent

class VsanHclFirmwareUpdateSpec(DynamicData):
   host: HostSystem
   hbaDevice: str
   fwFiles: list[VsanHclFirmwareFile] = []
   allowDowngrade: Optional[bool] = None
   firmwareComponent: list[VsanHostFwComponent] = []
