# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long
from pyVmomi.VmomiSupport import short

from pyVmomi.vim import Datastore
from pyVmomi.vim import DesiredSoftwareSpec
from pyVmomi.vim import EnvironmentBrowser
from pyVmomi.vim import HostSystem
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Network
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import ConnectSpec

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

   def ReconfigureEx(self, spec: ConfigSpec, modify: bool) -> Task: ...
