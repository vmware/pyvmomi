# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import HostBusAdapter
from pyVmomi.vim.host import ScsiLun
from pyVmomi.vim.host import TargetTransport

class PlugStoreTopology(DynamicData):
   class Adapter(DynamicData):
      key: str
      adapter: HostBusAdapter
      path: list[Path] = []

   class Path(DynamicData):
      key: str
      name: str
      channelNumber: Optional[int] = None
      targetNumber: Optional[int] = None
      lunNumber: Optional[int] = None
      adapter: Optional[Adapter] = None
      target: Optional[Target] = None
      device: Optional[Device] = None

   class Device(DynamicData):
      key: str
      lun: ScsiLun
      path: list[Path] = []

   class Plugin(DynamicData):
      key: str
      name: str
      device: list[Device] = []
      claimedPath: list[Path] = []

   class Target(DynamicData):
      key: str
      transport: Optional[TargetTransport] = None

   adapter: list[Adapter] = []
   path: list[Path] = []
   target: list[Target] = []
   device: list[Device] = []
   plugin: list[Plugin] = []
