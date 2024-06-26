# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VirtualNic
from pyVmomi.vim.host import VirtualNicConnection
from pyVmomi.vim.host import VirtualNicManagerInfo

class VirtualNicManager(ExtensibleManagedObject):
   class NicType(Enum):
      vmotion: ClassVar['NicType'] = 'vmotion'
      faultToleranceLogging: ClassVar['NicType'] = 'faultToleranceLogging'
      vSphereReplication: ClassVar['NicType'] = 'vSphereReplication'
      vSphereReplicationNFC: ClassVar['NicType'] = 'vSphereReplicationNFC'
      management: ClassVar['NicType'] = 'management'
      vsan: ClassVar['NicType'] = 'vsan'
      vSphereProvisioning: ClassVar['NicType'] = 'vSphereProvisioning'
      vsanWitness: ClassVar['NicType'] = 'vsanWitness'
      vSphereBackupNFC: ClassVar['NicType'] = 'vSphereBackupNFC'
      ptp: ClassVar['NicType'] = 'ptp'
      vsanReplication: ClassVar['NicType'] = 'vsanReplication'
      nvmeTcp: ClassVar['NicType'] = 'nvmeTcp'
      nvmeRdma: ClassVar['NicType'] = 'nvmeRdma'
      vsanExternal: ClassVar['NicType'] = 'vsanExternal'

   class NicTypeSelection(DynamicData):
      vnic: VirtualNicConnection
      nicType: list[str] = []

   class NetConfig(DynamicData):
      nicType: str
      multiSelectAllowed: bool
      candidateVnic: list[VirtualNic] = []
      selectedVnic: list[VirtualNic] = []

   @property
   def info(self) -> VirtualNicManagerInfo: ...

   def QueryNetConfig(self, nicType: str) -> Optional[NetConfig]: ...
   def SelectVnic(self, nicType: str, device: str) -> NoReturn: ...
   def DeselectVnic(self, nicType: str, device: str) -> NoReturn: ...
