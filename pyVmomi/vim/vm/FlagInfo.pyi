# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class FlagInfo(DynamicData):
   class HtSharing(Enum):
      any: ClassVar['HtSharing'] = 'any'
      none: ClassVar['HtSharing'] = 'none'
      internal: ClassVar['HtSharing'] = 'internal'

   class PowerOffBehavior(Enum):
      powerOff: ClassVar['PowerOffBehavior'] = 'powerOff'
      revert: ClassVar['PowerOffBehavior'] = 'revert'
      prompt: ClassVar['PowerOffBehavior'] = 'prompt'
      take: ClassVar['PowerOffBehavior'] = 'take'

   class MonitorType(Enum):
      release: ClassVar['MonitorType'] = 'release'
      debug: ClassVar['MonitorType'] = 'debug'
      stats: ClassVar['MonitorType'] = 'stats'

   class VirtualMmuUsage(Enum):
      automatic: ClassVar['VirtualMmuUsage'] = 'automatic'
      on: ClassVar['VirtualMmuUsage'] = 'on'
      off: ClassVar['VirtualMmuUsage'] = 'off'

   class VirtualExecUsage(Enum):
      hvAuto: ClassVar['VirtualExecUsage'] = 'hvAuto'
      hvOn: ClassVar['VirtualExecUsage'] = 'hvOn'
      hvOff: ClassVar['VirtualExecUsage'] = 'hvOff'

   disableAcceleration: Optional[bool] = None
   enableLogging: Optional[bool] = None
   useToe: Optional[bool] = None
   runWithDebugInfo: Optional[bool] = None
   monitorType: Optional[str] = None
   htSharing: Optional[str] = None
   snapshotDisabled: Optional[bool] = None
   snapshotLocked: Optional[bool] = None
   diskUuidEnabled: Optional[bool] = None
   virtualMmuUsage: Optional[str] = None
   virtualExecUsage: Optional[str] = None
   snapshotPowerOffBehavior: Optional[str] = None
   recordReplayEnabled: Optional[bool] = None
   faultToleranceType: Optional[str] = None
   cbrcCacheEnabled: Optional[bool] = None
   vvtdEnabled: Optional[bool] = None
   vbsEnabled: Optional[bool] = None
