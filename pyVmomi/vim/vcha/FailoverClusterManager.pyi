# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedMethod
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

class FailoverClusterManager(ManagedObject):
   class VchaNodeRole(Enum):
      active: ClassVar['VchaNodeRole'] = 'active'
      passive: ClassVar['VchaNodeRole'] = 'passive'
      witness: ClassVar['VchaNodeRole'] = 'witness'

   class VchaClusterMode(Enum):
      enabled: ClassVar['VchaClusterMode'] = 'enabled'
      disabled: ClassVar['VchaClusterMode'] = 'disabled'
      maintenance: ClassVar['VchaClusterMode'] = 'maintenance'

   class VchaClusterState(Enum):
      healthy: ClassVar['VchaClusterState'] = 'healthy'
      degraded: ClassVar['VchaClusterState'] = 'degraded'
      isolated: ClassVar['VchaClusterState'] = 'isolated'

   class VchaNodeState(Enum):
      up: ClassVar['VchaNodeState'] = 'up'
      down: ClassVar['VchaNodeState'] = 'down'

   class VchaNodeRuntimeInfo(DynamicData):
      nodeState: str
      nodeRole: str
      nodeIp: str

   class VchaClusterRuntimeInfo(DynamicData):
      clusterState: str
      nodeInfo: list[VchaNodeRuntimeInfo] = []
      clusterMode: str

   class VchaClusterHealth(DynamicData):
      runtimeInfo: VchaClusterRuntimeInfo
      healthMessages: list[LocalizableMessage] = []
      additionalInformation: list[LocalizableMessage] = []

   @property
   def disabledClusterMethod(self) -> list[ManagedMethod]: ...

   def SetClusterMode(self, mode: str) -> Task: ...
   def GetClusterMode(self) -> str: ...
   def GetClusterHealth(self) -> VchaClusterHealth: ...
   def InitiateFailover(self, planned: bool) -> Task: ...
