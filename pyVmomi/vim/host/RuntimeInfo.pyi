# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import HostSystem
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import DasFdmHostState

from pyVmomi.vim.encryption import CryptoKeyId

from pyVmomi.vim.host import HealthStatusSystem
from pyVmomi.vim.host import PartialMaintenanceModeRuntimeInfo
from pyVmomi.vim.host import TpmDigestInfo
from pyVmomi.vim.host import VFlashManager

from pyVmomi.vim.vsan.host import VsanRuntimeInfo

class RuntimeInfo(DynamicData):
   class NetStackInstanceRuntimeInfo(DynamicData):
      class State(Enum):
         inactive: ClassVar['State'] = 'inactive'
         active: ClassVar['State'] = 'active'
         deactivating: ClassVar['State'] = 'deactivating'
         activating: ClassVar['State'] = 'activating'

      netStackInstanceKey: str
      state: Optional[str] = None
      vmknicKeys: list[str] = []
      maxNumberOfConnections: Optional[int] = None
      currentIpV6Enabled: Optional[bool] = None

   class PlacedVirtualNicIdentifier(DynamicData):
      vm: VirtualMachine
      vnicKey: str
      reservation: Optional[int] = None

   class PnicNetworkResourceInfo(DynamicData):
      pnicDevice: str
      availableBandwidthForVMTraffic: Optional[long] = None
      unusedBandwidthForVMTraffic: Optional[long] = None
      placedVirtualNics: list[PlacedVirtualNicIdentifier] = []

   class NetworkResourceRuntimeInfo(DynamicData):
      pnicResourceInfo: list[PnicNetworkResourceInfo] = []

   class NetworkRuntimeInfo(DynamicData):
      netStackInstanceRuntimeInfo: list[NetStackInstanceRuntimeInfo] = []
      networkResourceRuntime: Optional[NetworkResourceRuntimeInfo] = None

   class StatelessNvdsMigrationState(Enum):
      ready: ClassVar['StatelessNvdsMigrationState'] = 'ready'
      notNeeded: ClassVar['StatelessNvdsMigrationState'] = 'notNeeded'
      unknown: ClassVar['StatelessNvdsMigrationState'] = 'unknown'

   class StateEncryptionInfo(DynamicData):
      class ProtectionMode(Enum):
         none: ClassVar['ProtectionMode'] = 'none'
         tpm: ClassVar['ProtectionMode'] = 'tpm'

      protectionMode: str
      requireSecureBoot: Optional[bool] = None
      requireExecInstalledOnly: Optional[bool] = None

   connectionState: HostSystem.ConnectionState
   powerState: HostSystem.PowerState
   standbyMode: Optional[str] = None
   inMaintenanceMode: bool
   inQuarantineMode: Optional[bool] = None
   bootTime: Optional[datetime] = None
   healthSystemRuntime: Optional[HealthStatusSystem.Runtime] = None
   dasHostState: Optional[DasFdmHostState] = None
   tpmPcrValues: list[TpmDigestInfo] = []
   vsanRuntimeInfo: Optional[VsanRuntimeInfo] = None
   networkRuntimeInfo: Optional[NetworkRuntimeInfo] = None
   vFlashResourceRuntimeInfo: Optional[VFlashManager.VFlashResourceRunTimeInfo] = None
   hostMaxVirtualDiskCapacity: Optional[long] = None
   cryptoState: Optional[str] = None
   cryptoKeyId: Optional[CryptoKeyId] = None
   statelessNvdsMigrationReady: Optional[str] = None
   partialMaintenanceMode: list[PartialMaintenanceModeRuntimeInfo] = []
   stateEncryption: Optional[StateEncryptionInfo] = None
