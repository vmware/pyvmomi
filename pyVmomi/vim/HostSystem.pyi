# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.HostServiceTicket import HostServiceTicket

from pyVmomi.vim.LicenseManager import LicenseManager

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.Network import Network

from pyVmomi.vim.Task import Task

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.encryption.CryptoKeyId import CryptoKeyId

from pyVmomi.vim.encryption.CryptoKeyPlain import CryptoKeyPlain

from pyVmomi.vim.host.Capability import Capability

from pyVmomi.vim.host.ConfigInfo import ConfigInfo

from pyVmomi.vim.host.ConfigManager import ConfigManager

from pyVmomi.vim.host.ConnectInfo import ConnectInfo

from pyVmomi.vim.host.ConnectSpec import ConnectSpec

from pyVmomi.vim.host.DatastoreBrowser import DatastoreBrowser

from pyVmomi.vim.host.FlagInfo import FlagInfo

from pyVmomi.vim.host.HardwareInfo import HardwareInfo

from pyVmomi.vim.host.IpmiInfo import IpmiInfo

from pyVmomi.vim.host.MaintenanceSpec import MaintenanceSpec

from pyVmomi.vim.host.RuntimeInfo import RuntimeInfo

from pyVmomi.vim.host.Summary import Summary

from pyVmomi.vim.host.SystemResourceInfo import SystemResourceInfo

from pyVmomi.vim.host.SystemSwapConfiguration import SystemSwapConfiguration

from pyVmomi.vim.host.TpmAttestationReport import TpmAttestationReport

from pyVmomi.vim.profile.ComplianceResult import ComplianceResult

from pyVmomi.vim.vm.ConfigInfo import ConfigInfo

from pyVmomi.vim.profile.host.AnswerFileStatusResult import AnswerFileStatusResult

from pyVmomi.vim.profile.host.ProfileManager import ProfileManager

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
   def UpdateSystemResources(self, resourceInfo: SystemResourceInfo) -> None: ...
   def UpdateSystemSwapConfiguration(self, sysSwapConfig: SystemSwapConfiguration) -> None: ...
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
   def UpdateFlags(self, flagInfo: FlagInfo) -> None: ...
   def EnterLockdownMode(self) -> None: ...
   def ExitLockdownMode(self) -> None: ...
   def AcquireCimServicesTicket(self) -> HostServiceTicket: ...
   def UpdateIpmi(self, ipmiInfo: IpmiInfo) -> None: ...
   def RetrieveHardwareUptime(self) -> long: ...
   def PrepareCrypto(self) -> None: ...
   def EnableCrypto(self, keyPlain: CryptoKeyPlain) -> None: ...
   def ConfigureCryptoKey(self, keyId: Optional[CryptoKeyId]) -> None: ...
   def QueryProductLockerLocation(self) -> str: ...
   def UpdateProductLockerLocation(self, path: str) -> Task: ...
   def RetrieveFreeEpcMemory(self) -> long: ...
