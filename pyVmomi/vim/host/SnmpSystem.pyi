# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.KeyValue import KeyValue

from pyVmomi.vmodl.DynamicData import DynamicData

class SnmpSystem(ManagedObject):
   class SnmpConfigSpec(DynamicData):
      class Destination(DynamicData):
         hostName: str
         port: int
         community: str

      enabled: Optional[bool] = None
      port: Optional[int] = None
      readOnlyCommunities: list[str] = []
      trapTargets: list[Destination] = []
      option: list[KeyValue] = []

   class AgentLimits(DynamicData):
      class Capability(Enum):
         COMPLETE: ClassVar['Capability'] = 'COMPLETE'
         DIAGNOSTICS: ClassVar['Capability'] = 'DIAGNOSTICS'
         CONFIGURATION: ClassVar['Capability'] = 'CONFIGURATION'

      maxReadOnlyCommunities: int
      maxTrapDestinations: int
      maxCommunityLength: int
      maxBufferSize: int
      capability: Capability

   @property
   def configuration(self) -> SnmpConfigSpec: ...
   @property
   def limits(self) -> AgentLimits: ...

   def ReconfigureSnmpAgent(self, spec: SnmpConfigSpec) -> None: ...
   def SendTestNotification(self) -> None: ...
