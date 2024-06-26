# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Capability
from pyVmomi.vim import HostSystem
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import ServiceInstanceContent
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.event import Event

class ServiceInstance(ManagedObject):
   class ValidateMigrationTestType(Enum):
      sourceTests: ClassVar['ValidateMigrationTestType'] = 'sourceTests'
      compatibilityTests: ClassVar['ValidateMigrationTestType'] = 'compatibilityTests'
      diskAccessibilityTests: ClassVar['ValidateMigrationTestType'] = 'diskAccessibilityTests'
      resourceTests: ClassVar['ValidateMigrationTestType'] = 'resourceTests'

   class VMotionCompatibilityType(Enum):
      cpu: ClassVar['VMotionCompatibilityType'] = 'cpu'
      software: ClassVar['VMotionCompatibilityType'] = 'software'

   class HostVMotionCompatibility(DynamicData):
      host: HostSystem
      compatibility: list[str] = []

   class ProductComponentInfo(DynamicData):
      id: str
      name: str
      version: str
      release: int

   @property
   def serverClock(self) -> datetime: ...
   @property
   def capability(self) -> Capability: ...
   @property
   def content(self) -> ServiceInstanceContent: ...

   def CurrentTime(self) -> datetime: ...
   def RetrieveContent(self) -> ServiceInstanceContent: ...
   def ValidateMigration(self, vm: list[VirtualMachine], state: Optional[VirtualMachine.PowerState], testType: list[str], pool: Optional[ResourcePool], host: Optional[HostSystem]) -> list[Event]: ...
   def QueryVMotionCompatibility(self, vm: VirtualMachine, host: list[HostSystem], compatibility: list[str]) -> list[HostVMotionCompatibility]: ...
   def RetrieveProductComponents(self) -> list[ProductComponentInfo]: ...
