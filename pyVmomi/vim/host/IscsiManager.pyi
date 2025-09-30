# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.host.PhysicalNic import PhysicalNic

from pyVmomi.vim.host.VirtualNic import VirtualNic

class IscsiManager(ManagedObject):
   class IscsiStatus(DynamicData):
      reason: list[MethodFault] = []

   class IscsiPortInfo(DynamicData):
      class PathStatus(Enum):
         notUsed: ClassVar['PathStatus'] = 'notUsed'
         active: ClassVar['PathStatus'] = 'active'
         standBy: ClassVar['PathStatus'] = 'standBy'
         lastActive: ClassVar['PathStatus'] = 'lastActive'

      vnicDevice: Optional[str] = None
      vnic: Optional[VirtualNic] = None
      pnicDevice: Optional[str] = None
      pnic: Optional[PhysicalNic] = None
      switchName: Optional[str] = None
      switchUuid: Optional[str] = None
      portgroupName: Optional[str] = None
      portgroupKey: Optional[str] = None
      portKey: Optional[str] = None
      opaqueNetworkId: Optional[str] = None
      opaqueNetworkType: Optional[str] = None
      opaqueNetworkName: Optional[str] = None
      externalId: Optional[str] = None
      complianceStatus: Optional[IscsiStatus] = None
      pathStatus: Optional[str] = None

   class IscsiDependencyEntity(DynamicData):
      pnicDevice: str
      vnicDevice: str
      vmhbaName: str

   class IscsiMigrationDependency(DynamicData):
      migrationAllowed: bool
      disallowReason: Optional[IscsiStatus] = None
      dependency: list[IscsiDependencyEntity] = []

   def QueryVnicStatus(self, vnicDevice: str) -> IscsiStatus: ...
   def QueryPnicStatus(self, pnicDevice: str) -> IscsiStatus: ...
   def QueryBoundVnics(self, iScsiHbaName: str) -> list[IscsiPortInfo]: ...
   def QueryCandidateNics(self, iScsiHbaName: str) -> list[IscsiPortInfo]: ...
   def BindVnic(self, iScsiHbaName: str, vnicDevice: str) -> None: ...
   def UnbindVnic(self, iScsiHbaName: str, vnicDevice: str, force: bool) -> None: ...
   def QueryMigrationDependencies(self, pnicDevice: list[str]) -> IscsiMigrationDependency: ...
