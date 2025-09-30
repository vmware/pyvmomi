# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long
from pyVmomi.VmomiSupport import short

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.DesiredSoftwareSpec import DesiredSoftwareSpec

from pyVmomi.vim.EnvironmentBrowser import EnvironmentBrowser

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.Network import Network

from pyVmomi.vim.ResourcePool import ResourcePool

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.ConnectSpec import ConnectSpec

class ComputeResource(ManagedEntity):
   class Summary(DynamicData):
      totalCpu: int
      totalMemory: long
      numCpuCores: short
      numCpuThreads: short
      effectiveCpu: int
      effectiveMemory: long
      numHosts: int
      numEffectiveHosts: int
      overallStatus: ManagedEntity.Status

   class NetworkBootMode(Enum):
      bootstrap: ClassVar['NetworkBootMode'] = 'bootstrap'
      stateless: ClassVar['NetworkBootMode'] = 'stateless'

   class ConfigInfo(DynamicData):
      vmSwapPlacement: str
      spbmEnabled: Optional[bool] = None
      defaultHardwareVersionKey: Optional[str] = None
      maximumHardwareVersionKey: Optional[str] = None

   class HostSPBMLicenseInfo(DynamicData):
      class HostSPBMLicenseState(Enum):
         licensed: ClassVar['HostSPBMLicenseState'] = 'licensed'
         unlicensed: ClassVar['HostSPBMLicenseState'] = 'unlicensed'
         unknown: ClassVar['HostSPBMLicenseState'] = 'unknown'

      host: HostSystem
      licenseState: HostSPBMLicenseState

   class HostSeedSpec(DynamicData):
      class SingleHostSpec(DynamicData):
         newHostCnxSpec: Optional[ConnectSpec] = None
         existingHost: Optional[HostSystem] = None

      singleHostSpec: SingleHostSpec

   class ConfigSpec(DynamicData):
      vmSwapPlacement: Optional[str] = None
      spbmEnabled: Optional[bool] = None
      defaultHardwareVersionKey: Optional[str] = None
      desiredSoftwareSpec: Optional[DesiredSoftwareSpec] = None
      maximumHardwareVersionKey: Optional[str] = None
      enableConfigManager: Optional[bool] = None
      hostSeedSpec: Optional[HostSeedSpec] = None
      softwareSpecId: Optional[str] = None
      networkBootMode: Optional[str] = None

   @property
   def resourcePool(self) -> Optional[ResourcePool]: ...
   @property
   def host(self) -> list[HostSystem]: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def environmentBrowser(self) -> Optional[EnvironmentBrowser]: ...
   @property
   def configurationEx(self) -> ConfigInfo: ...
   @property
   def lifecycleManaged(self) -> Optional[bool]: ...
   @property
   def configManagerEnabled(self) -> Optional[bool]: ...
   @property
   def networkBootMode(self) -> Optional[str]: ...

   def EnableNetworkBoot(self, networkBootMode: str) -> Task: ...
   def DisableNetworkBoot(self) -> Task: ...
   def ReconfigureEx(self, spec: ConfigSpec, modify: bool) -> Task: ...
