# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.eam import Agency
from pyVmomi.eam import EamObject

from pyVmomi.vim import Folder
from pyVmomi.vim import HostSystem
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.eam.vib import VibInfo

class Agent(EamObject):
   class RuntimeInfo(EamObject.RuntimeInfo):
      vmPowerState: VirtualMachine.PowerState
      receivingHeartBeat: bool
      host: Optional[HostSystem] = None
      vm: Optional[VirtualMachine] = None
      vmIp: Optional[str] = None
      vmName: str
      esxAgentResourcePool: Optional[ResourcePool] = None
      esxAgentFolder: Optional[Folder] = None
      installedBulletin: list[str] = []
      installedVibs: list[VibInfo] = []
      agency: Optional[Agency] = None
      vmHook: Optional[VmHook] = None

   class VmHook(DynamicData):
      class VmState(Enum):
         provisioned: ClassVar['VmState'] = 'provisioned'
         poweredOn: ClassVar['VmState'] = 'poweredOn'
         prePowerOn: ClassVar['VmState'] = 'prePowerOn'

      vm: VirtualMachine
      vmState: str

   class StoragePolicy(DynamicData):
      pass

   class VsanStoragePolicy(StoragePolicy):
      profileId: str

   class SslTrust(DynamicData):
      pass

   class PinnedPemCertificate(SslTrust):
      sslCertificate: str

   class AnyCertificate(SslTrust):
      pass

   class ConfigInfo(DynamicData):
      class OvfDiskProvisioning(Enum):
         none: ClassVar['OvfDiskProvisioning'] = 'none'
         thin: ClassVar['OvfDiskProvisioning'] = 'thin'
         thick: ClassVar['OvfDiskProvisioning'] = 'thick'

      productLineId: Optional[str] = None
      hostVersion: Optional[str] = None
      ovfPackageUrl: Optional[str] = None
      ovfSslTrust: Optional[SslTrust] = None
      ovfEnvironment: Optional[OvfEnvironmentInfo] = None
      vibUrl: Optional[str] = None
      vibSslTrust: Optional[SslTrust] = None
      vibMatchingRules: list[VibMatchingRule] = []
      vibName: Optional[str] = None
      dvFilterEnabled: Optional[bool] = None
      rebootHostAfterVibUninstall: Optional[bool] = None
      vmciService: list[str] = []
      ovfDiskProvisioning: Optional[str] = None
      vmStoragePolicies: list[StoragePolicy] = []
      vmResourceConfiguration: Optional[str] = None

   class OvfEnvironmentInfo(DynamicData):
      class OvfProperty(DynamicData):
         key: str
         value: str

      ovfProperty: list[OvfProperty] = []

   class VibMatchingRule(DynamicData):
      vibNameRegex: str
      vibVersionRegex: str

   @property
   def runtime(self) -> RuntimeInfo: ...
   @property
   def config(self) -> ConfigInfo: ...

   def QueryRuntime(self) -> RuntimeInfo: ...
   def MarkAsAvailable(self) -> NoReturn: ...
   def QueryConfig(self) -> ConfigInfo: ...
