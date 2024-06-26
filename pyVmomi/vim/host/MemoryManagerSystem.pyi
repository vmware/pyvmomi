# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vmodl import DynamicData

class MemoryManagerSystem(ExtensibleManagedObject):
   class ServiceConsoleReservationInfo(DynamicData):
      serviceConsoleReservedCfg: long
      serviceConsoleReserved: long
      unreserved: long

   class VirtualMachineReservationInfo(DynamicData):
      class AllocationPolicy(Enum):
         swapNone: ClassVar['AllocationPolicy'] = 'swapNone'
         swapSome: ClassVar['AllocationPolicy'] = 'swapSome'
         swapMost: ClassVar['AllocationPolicy'] = 'swapMost'

      virtualMachineMin: long
      virtualMachineMax: long
      virtualMachineReserved: long
      allocationPolicy: str

   class VirtualMachineReservationSpec(DynamicData):
      virtualMachineReserved: Optional[long] = None
      allocationPolicy: Optional[str] = None

   @property
   def consoleReservationInfo(self) -> Optional[ServiceConsoleReservationInfo]: ...
   @property
   def virtualMachineReservationInfo(self) -> Optional[VirtualMachineReservationInfo]: ...

   def ReconfigureServiceConsoleReservation(self, cfgBytes: long) -> NoReturn: ...
   def ReconfigureVirtualMachineReservation(self, spec: VirtualMachineReservationSpec) -> NoReturn: ...
