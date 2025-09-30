# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.HostBusAdapter import HostBusAdapter

from pyVmomi.vim.host.ScsiLun import ScsiLun

from pyVmomi.vim.host.TargetTransport import TargetTransport

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
