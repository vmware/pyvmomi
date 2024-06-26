# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore
from pyVmomi.vim import HostServiceTicket
from pyVmomi.vim import LicenseManager
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Network
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.encryption import CryptoKeyId
from pyVmomi.vim.encryption import CryptoKeyPlain

from pyVmomi.vim.host import Capability
from pyVmomi.vim.host import ConfigInfo
from pyVmomi.vim.host import ConfigManager
from pyVmomi.vim.host import ConnectInfo
from pyVmomi.vim.host import ConnectSpec
from pyVmomi.vim.host import DatastoreBrowser
from pyVmomi.vim.host import FlagInfo
from pyVmomi.vim.host import HardwareInfo
from pyVmomi.vim.host import IpmiInfo
from pyVmomi.vim.host import MaintenanceSpec
from pyVmomi.vim.host import RuntimeInfo
from pyVmomi.vim.host import Summary
from pyVmomi.vim.host import SystemResourceInfo
from pyVmomi.vim.host import SystemSwapConfiguration
from pyVmomi.vim.host import TpmAttestationReport

from pyVmomi.vim.profile import ComplianceResult

from pyVmomi.vim.vm import ConfigInfo

from pyVmomi.vim.profile.host import AnswerFileStatusResult
from pyVmomi.vim.profile.host import ProfileManager

class HostSystem(ManagedEntity):
   class ConnectionState(Enum):
      connected: ClassVar['ConnectionState'] = 'connected'
      notResponding: ClassVar['ConnectionState'] = 'notResponding'
      disconnected: ClassVar['ConnectionState'] = 'disconnected'

   class PowerState(Enum):
      poweredOn: ClassVar['PowerState'] = 'poweredOn'
      poweredOff: ClassVar['PowerState'] = 'poweredOff'
      standBy: ClassVar['PowerState'] = 'standBy'
      unknown: ClassVar['PowerState'] = 'unknown'

   class StandbyMode(Enum):
      entering: ClassVar['StandbyMode'] = 'entering'
      exiting: ClassVar['StandbyMode'] = 'exiting'
      # Reserved python keyword: commenting out.
      # in: ClassVar['StandbyMode'] = 'in'
      none: ClassVar['StandbyMode'] = 'none'

   class CryptoState(Enum):
      incapable: ClassVar['CryptoState'] = 'incapable'
      prepared: ClassVar['CryptoState'] = 'prepared'
      safe: ClassVar['CryptoState'] = 'safe'
      pendingIncapable: ClassVar['CryptoState'] = 'pendingIncapable'

   class RemediationState(DynamicData):
      class State(Enum):
         remediationReady: ClassVar['State'] = 'remediationReady'
         precheckRemediationRunning: ClassVar['State'] = 'precheckRemediationRunning'
         precheckRemediationComplete: ClassVar['State'] = 'precheckRemediationComplete'
         precheckRemediationFailed: ClassVar['State'] = 'precheckRemediationFailed'
         remediationRunning: ClassVar['State'] = 'remediationRunning'
         remediationFailed: ClassVar['State'] = 'remediationFailed'

      state: str
      operationTime: datetime

   class ComplianceCheckState(DynamicData):
      state: str
      checkTime: datetime

   class ReconnectSpec(DynamicData):
      syncState: Optional[bool] = None

   @property
   def runtime(self) -> RuntimeInfo: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def hardware(self) -> Optional[HardwareInfo]: ...
   @property
   def capability(self) -> Optional[Capability]: ...
   @property
   def licensableResource(self) -> LicenseManager.LicensableResourceInfo: ...
   @property
   def remediationState(self) -> Optional[RemediationState]: ...
   @property
   def precheckRemediationResult(self) -> Optional[ProfileManager.ApplyHostConfigSpec]: ...
   @property
   def remediationResult(self) -> Optional[ProfileManager.ApplyHostConfigResult]: ...
   @property
   def complianceCheckState(self) -> Optional[ComplianceCheckState]: ...
   @property
   def complianceCheckResult(self) -> Optional[ComplianceResult]: ...
   @property
   def configManager(self) -> ConfigManager: ...
   @property
   def config(self) -> Optional[ConfigInfo]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def datastoreBrowser(self) -> DatastoreBrowser: ...
   @property
   def systemResources(self) -> Optional[SystemResourceInfo]: ...
   @property
   def answerFileValidationState(self) -> Optional[AnswerFileStatusResult]: ...
   @property
   def answerFileValidationResult(self) -> Optional[AnswerFileStatusResult]: ...

   def QueryTpmAttestationReport(self) -> Optional[TpmAttestationReport]: ...
   def QueryConnectionInfo(self) -> ConnectInfo: ...
   def UpdateSystemResources(self, resourceInfo: SystemResourceInfo) -> NoReturn: ...
   def UpdateSystemSwapConfiguration(self, sysSwapConfig: SystemSwapConfiguration) -> NoReturn: ...
   def Reconnect(self, cnxSpec: Optional[ConnectSpec], reconnectSpec: Optional[ReconnectSpec]) -> Task: ...
   def Disconnect(self) -> Task: ...
   def EnterMaintenanceMode(self, timeout: int, evacuatePoweredOffVms: Optional[bool], maintenanceSpec: Optional[MaintenanceSpec]) -> Task: ...
   def ExitMaintenanceMode(self, timeout: int) -> Task: ...
   def Reboot(self, force: bool) -> Task: ...
   def Shutdown(self, force: bool) -> Task: ...
   def EnterStandbyMode(self, timeoutSec: int, evacuatePoweredOffVms: Optional[bool]) -> Task: ...
   def ExitStandbyMode(self, timeoutSec: int) -> Task: ...
   def QueryOverhead(self, memorySize: long, videoRamSize: Optional[int], numVcpus: int) -> long: ...
   def QueryOverheadEx(self, vmConfigInfo: ConfigInfo) -> long: ...
   def ReconfigureDAS(self) -> Task: ...
   def UpdateFlags(self, flagInfo: FlagInfo) -> NoReturn: ...
   def EnterLockdownMode(self) -> NoReturn: ...
   def ExitLockdownMode(self) -> NoReturn: ...
   def AcquireCimServicesTicket(self) -> HostServiceTicket: ...
   def UpdateIpmi(self, ipmiInfo: IpmiInfo) -> NoReturn: ...
   def RetrieveHardwareUptime(self) -> long: ...
   def PrepareCrypto(self) -> NoReturn: ...
   def EnableCrypto(self, keyPlain: CryptoKeyPlain) -> NoReturn: ...
   def ConfigureCryptoKey(self, keyId: Optional[CryptoKeyId]) -> NoReturn: ...
   def QueryProductLockerLocation(self) -> str: ...
   def UpdateProductLockerLocation(self, path: str) -> Task: ...
   def RetrieveFreeEpcMemory(self) -> long: ...
