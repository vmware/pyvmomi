# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import DistributedVirtualSwitch
from pyVmomi.vim import HostSystem
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import SelectionSet
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.dvs import DistributedVirtualPortgroup
from pyVmomi.vim.dvs import DistributedVirtualPortgroupInfo
from pyVmomi.vim.dvs import DistributedVirtualSwitchInfo
from pyVmomi.vim.dvs import EntityBackup
from pyVmomi.vim.dvs import HostProductSpec
from pyVmomi.vim.dvs import NetworkOffloadSpec
from pyVmomi.vim.dvs import ProductSpec

from pyVmomi.vim.fault import ImportOperationBulkFault

from pyVmomi.vim.host import PhysicalNic

class DistributedVirtualSwitchManager(ManagedObject):
   class PhysicalNicsList(DynamicData):
      host: HostSystem
      physicalNics: list[PhysicalNic] = []

   class DvsConfigTarget(DynamicData):
      distributedVirtualPortgroup: list[DistributedVirtualPortgroupInfo] = []
      distributedVirtualSwitch: list[DistributedVirtualSwitchInfo] = []

   class CompatibilityResult(DynamicData):
      host: HostSystem
      error: list[MethodFault] = []

   class HostContainer(DynamicData):
      container: ManagedEntity
      recursive: bool

   class HostDvsFilterSpec(DynamicData):
      inclusive: bool

   class HostArrayFilter(HostDvsFilterSpec):
      host: list[HostSystem] = []

   class HostContainerFilter(HostDvsFilterSpec):
      hostContainer: HostContainer

   class HostDvsMembershipFilter(HostDvsFilterSpec):
      distributedVirtualSwitch: DistributedVirtualSwitch

   class DvsProductSpec(DynamicData):
      newSwitchProductSpec: Optional[ProductSpec] = None
      distributedVirtualSwitch: Optional[DistributedVirtualSwitch] = None

   class ImportResult(DynamicData):
      distributedVirtualSwitch: list[DistributedVirtualSwitch] = []
      distributedVirtualPortgroup: list[DistributedVirtualPortgroup] = []
      importFault: list[ImportOperationBulkFault.FaultOnImport] = []

   def QuerySupportedSwitchSpec(self, recommended: Optional[bool]) -> list[ProductSpec]: ...
   def QuerySupportedNetworkOffloadSpec(self, switchProductSpec: ProductSpec) -> list[NetworkOffloadSpec]: ...
   def QueryCompatibleVmnicsFromHosts(self, hosts: list[HostSystem], dvs: DistributedVirtualSwitch) -> list[PhysicalNicsList]: ...
   def QueryCompatibleHostForNewDvs(self, container: ManagedEntity, recursive: bool, switchProductSpec: Optional[ProductSpec]) -> list[HostSystem]: ...
   def QueryCompatibleHostForExistingDvs(self, container: ManagedEntity, recursive: bool, dvs: DistributedVirtualSwitch) -> list[HostSystem]: ...
   def QueryCompatibleHostSpec(self, switchProductSpec: Optional[ProductSpec]) -> list[HostProductSpec]: ...
   def QueryFeatureCapability(self, switchProductSpec: Optional[ProductSpec]) -> Optional[DistributedVirtualSwitch.FeatureCapability]: ...
   def QuerySwitchByUuid(self, uuid: str) -> Optional[DistributedVirtualSwitch]: ...
   def QueryDvsConfigTarget(self, host: Optional[HostSystem], dvs: Optional[DistributedVirtualSwitch]) -> DvsConfigTarget: ...
   def CheckCompatibility(self, hostContainer: HostContainer, dvsProductSpec: Optional[DvsProductSpec], hostFilterSpec: list[HostDvsFilterSpec]) -> list[CompatibilityResult]: ...
   def RectifyHost(self, hosts: list[HostSystem]) -> Task: ...
   def ExportEntity(self, selectionSet: list[SelectionSet]) -> Task: ...
   def ImportEntity(self, entityBackup: list[EntityBackup.Config], importType: str) -> Task: ...
   def LookupPortgroup(self, switchUuid: str, portgroupKey: str) -> Optional[DistributedVirtualPortgroup]: ...
