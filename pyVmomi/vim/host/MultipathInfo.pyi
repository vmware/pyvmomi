# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import HostBusAdapter
from pyVmomi.vim.host import ScsiLun
from pyVmomi.vim.host import TargetTransport

class MultipathInfo(DynamicData):
   class PathState(Enum):
      standby: ClassVar['PathState'] = 'standby'
      active: ClassVar['PathState'] = 'active'
      disabled: ClassVar['PathState'] = 'disabled'
      dead: ClassVar['PathState'] = 'dead'
      unknown: ClassVar['PathState'] = 'unknown'

   class LogicalUnitPolicy(DynamicData):
      policy: str

   class HppLogicalUnitPolicy(LogicalUnitPolicy):
      bytes: Optional[long] = None
      iops: Optional[long] = None
      path: Optional[str] = None
      latencyEvalTime: Optional[long] = None
      samplingIosPerPath: Optional[long] = None

   class LogicalUnitStorageArrayTypePolicy(DynamicData):
      policy: str

   class FixedLogicalUnitPolicy(LogicalUnitPolicy):
      prefer: str

   class LogicalUnit(DynamicData):
      key: str
      id: str
      lun: ScsiLun
      path: list[Path] = []
      policy: LogicalUnitPolicy
      storageArrayTypePolicy: Optional[LogicalUnitStorageArrayTypePolicy] = None

   class Path(DynamicData):
      key: str
      name: str
      pathState: str
      state: Optional[str] = None
      isWorkingPath: Optional[bool] = None
      adapter: HostBusAdapter
      lun: LogicalUnit
      transport: Optional[TargetTransport] = None

   lun: list[LogicalUnit] = []
