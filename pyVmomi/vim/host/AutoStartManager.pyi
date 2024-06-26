# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

class AutoStartManager(ManagedObject):
   class Action(Enum):
      none: ClassVar['Action'] = 'none'
      systemDefault: ClassVar['Action'] = 'systemDefault'
      powerOn: ClassVar['Action'] = 'powerOn'
      powerOff: ClassVar['Action'] = 'powerOff'
      guestShutdown: ClassVar['Action'] = 'guestShutdown'
      suspend: ClassVar['Action'] = 'suspend'

   class SystemDefaults(DynamicData):
      enabled: Optional[bool] = None
      startDelay: Optional[int] = None
      stopDelay: Optional[int] = None
      waitForHeartbeat: Optional[bool] = None
      stopAction: Optional[str] = None

   class AutoPowerInfo(DynamicData):
      class WaitHeartbeatSetting(Enum):
         yes: ClassVar['WaitHeartbeatSetting'] = 'yes'
         no: ClassVar['WaitHeartbeatSetting'] = 'no'
         systemDefault: ClassVar['WaitHeartbeatSetting'] = 'systemDefault'

      key: VirtualMachine
      startOrder: int
      startDelay: int
      waitForHeartbeat: WaitHeartbeatSetting
      startAction: str
      stopDelay: int
      stopAction: str

   class Config(DynamicData):
      defaults: Optional[SystemDefaults] = None
      powerInfo: list[AutoPowerInfo] = []

   @property
   def config(self) -> Config: ...

   def Reconfigure(self, spec: Config) -> NoReturn: ...
   def AutoPowerOn(self) -> NoReturn: ...
   def AutoPowerOff(self) -> NoReturn: ...
