# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.net import DhcpConfigInfo
from pyVmomi.vim.net import DnsConfigInfo
from pyVmomi.vim.net import IpConfigInfo
from pyVmomi.vim.net import IpRouteConfigInfo
from pyVmomi.vim.net import NetBIOSConfigInfo

class GuestInfo(DynamicData):
   class ToolsStatus(Enum):
      toolsNotInstalled: ClassVar['ToolsStatus'] = 'toolsNotInstalled'
      toolsNotRunning: ClassVar['ToolsStatus'] = 'toolsNotRunning'
      toolsOld: ClassVar['ToolsStatus'] = 'toolsOld'
      toolsOk: ClassVar['ToolsStatus'] = 'toolsOk'

   class ToolsVersionStatus(Enum):
      guestToolsNotInstalled: ClassVar['ToolsVersionStatus'] = 'guestToolsNotInstalled'
      guestToolsNeedUpgrade: ClassVar['ToolsVersionStatus'] = 'guestToolsNeedUpgrade'
      guestToolsCurrent: ClassVar['ToolsVersionStatus'] = 'guestToolsCurrent'
      guestToolsUnmanaged: ClassVar['ToolsVersionStatus'] = 'guestToolsUnmanaged'
      guestToolsTooOld: ClassVar['ToolsVersionStatus'] = 'guestToolsTooOld'
      guestToolsSupportedOld: ClassVar['ToolsVersionStatus'] = 'guestToolsSupportedOld'
      guestToolsSupportedNew: ClassVar['ToolsVersionStatus'] = 'guestToolsSupportedNew'
      guestToolsTooNew: ClassVar['ToolsVersionStatus'] = 'guestToolsTooNew'
      guestToolsBlacklisted: ClassVar['ToolsVersionStatus'] = 'guestToolsBlacklisted'

   class ToolsRunningStatus(Enum):
      guestToolsNotRunning: ClassVar['ToolsRunningStatus'] = 'guestToolsNotRunning'
      guestToolsRunning: ClassVar['ToolsRunningStatus'] = 'guestToolsRunning'
      guestToolsExecutingScripts: ClassVar['ToolsRunningStatus'] = 'guestToolsExecutingScripts'

   class ToolsInstallType(Enum):
      guestToolsTypeUnknown: ClassVar['ToolsInstallType'] = 'guestToolsTypeUnknown'
      guestToolsTypeMSI: ClassVar['ToolsInstallType'] = 'guestToolsTypeMSI'
      guestToolsTypeTar: ClassVar['ToolsInstallType'] = 'guestToolsTypeTar'
      guestToolsTypeOSP: ClassVar['ToolsInstallType'] = 'guestToolsTypeOSP'
      guestToolsTypeOpenVMTools: ClassVar['ToolsInstallType'] = 'guestToolsTypeOpenVMTools'

   class VirtualDiskMapping(DynamicData):
      key: int

   class DiskInfo(DynamicData):
      diskPath: Optional[str] = None
      capacity: Optional[long] = None
      freeSpace: Optional[long] = None
      filesystemType: Optional[str] = None
      mappings: list[VirtualDiskMapping] = []

   class NicInfo(DynamicData):
      network: Optional[str] = None
      ipAddress: list[str] = []
      macAddress: Optional[str] = None
      connected: bool
      deviceConfigId: int
      dnsConfig: Optional[DnsConfigInfo] = None
      ipConfig: Optional[IpConfigInfo] = None
      netBIOSConfig: Optional[NetBIOSConfigInfo] = None

   class StackInfo(DynamicData):
      dnsConfig: Optional[DnsConfigInfo] = None
      ipRouteConfig: Optional[IpRouteConfigInfo] = None
      ipStackConfig: list[KeyValue] = []
      dhcpConfig: Optional[DhcpConfigInfo] = None

   class ScreenInfo(DynamicData):
      width: int
      height: int

   class GuestState(Enum):
      running: ClassVar['GuestState'] = 'running'
      shuttingDown: ClassVar['GuestState'] = 'shuttingDown'
      resetting: ClassVar['GuestState'] = 'resetting'
      standby: ClassVar['GuestState'] = 'standby'
      notRunning: ClassVar['GuestState'] = 'notRunning'
      unknown: ClassVar['GuestState'] = 'unknown'

   class AppStateType(Enum):
      none: ClassVar['AppStateType'] = 'none'
      appStateOk: ClassVar['AppStateType'] = 'appStateOk'
      appStateNeedReset: ClassVar['AppStateType'] = 'appStateNeedReset'

   class NamespaceGenerationInfo(DynamicData):
      key: str
      generationNo: int

   class CustomizationStatus(Enum):
      TOOLSDEPLOYPKG_IDLE: ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_IDLE'
      TOOLSDEPLOYPKG_PENDING: ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_PENDING'
      TOOLSDEPLOYPKG_RUNNING: ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_RUNNING'
      TOOLSDEPLOYPKG_SUCCEEDED: ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_SUCCEEDED'
      TOOLSDEPLOYPKG_FAILED: ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_FAILED'

   class CustomizationInfo(DynamicData):
      customizationStatus: str
      startTime: Optional[datetime] = None
      endTime: Optional[datetime] = None
      errorMsg: Optional[str] = None

   toolsStatus: Optional[ToolsStatus] = None
   toolsVersionStatus: Optional[str] = None
   toolsVersionStatus2: Optional[str] = None
   toolsRunningStatus: Optional[str] = None
   toolsVersion: Optional[str] = None
   toolsInstallType: Optional[str] = None
   guestId: Optional[str] = None
   guestFamily: Optional[str] = None
   guestFullName: Optional[str] = None
   guestDetailedData: Optional[str] = None
   hostName: Optional[str] = None
   ipAddress: Optional[str] = None
   net: list[NicInfo] = []
   ipStack: list[StackInfo] = []
   disk: list[DiskInfo] = []
   screen: Optional[ScreenInfo] = None
   guestState: str
   appHeartbeatStatus: Optional[str] = None
   guestKernelCrashed: Optional[bool] = None
   appState: Optional[str] = None
   guestOperationsReady: Optional[bool] = None
   interactiveGuestOperationsReady: Optional[bool] = None
   guestStateChangeSupported: Optional[bool] = None
   generationInfo: list[NamespaceGenerationInfo] = []
   hwVersion: Optional[str] = None
   customizationInfo: Optional[CustomizationInfo] = None
