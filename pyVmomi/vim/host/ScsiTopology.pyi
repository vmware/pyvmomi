# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import HostBusAdapter
from pyVmomi.vim.host import ScsiLun
from pyVmomi.vim.host import TargetTransport

class ScsiTopology(DynamicData):
   class Interface(DynamicData):
      key: str
      adapter: HostBusAdapter
      target: list[Target] = []

   class Target(DynamicData):
      key: str
      target: int
      lun: list[Lun] = []
      transport: Optional[TargetTransport] = None

   class Lun(DynamicData):
      key: str
      lun: int
      scsiLun: ScsiLun

   adapter: list[Interface] = []
