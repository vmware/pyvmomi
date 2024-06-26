# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long
from pyVmomi.VmomiSupport import short

from pyVmomi.vim import AboutInfo
from pyVmomi.vim import CustomFieldsManager
from pyVmomi.vim import Datastore
from pyVmomi.vim import HostSystem
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Network

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import FeatureVersionInfo
from pyVmomi.vim.host import RuntimeInfo
from pyVmomi.vim.host import SystemIdentificationInfo
from pyVmomi.vim.host import TpmAttestationInfo
from pyVmomi.vim.host import TrustAuthorityAttestationInfo

class Summary(DynamicData):
   class HardwareSummary(DynamicData):
      vendor: str
      model: str
      uuid: str
      otherIdentifyingInfo: list[SystemIdentificationInfo] = []
      memorySize: long
      cpuModel: str
      cpuMhz: int
      numCpuPkgs: short
      numCpuCores: short
      numCpuThreads: short
      numNics: int
      numHBAs: int

   class QuickStats(DynamicData):
      overallCpuUsage: Optional[int] = None
      overallMemoryUsage: Optional[int] = None
      distributedCpuFairness: Optional[int] = None
      distributedMemoryFairness: Optional[int] = None
      availablePMemCapacity: Optional[int] = None
      uptime: Optional[int] = None

   class ConfigSummary(DynamicData):
      name: str
      port: int
      sslThumbprint: Optional[str] = None
      product: Optional[AboutInfo] = None
      vmotionEnabled: bool
      faultToleranceEnabled: bool
      featureVersion: list[FeatureVersionInfo] = []
      agentVmDatastore: Optional[Datastore] = None
      agentVmNetwork: Optional[Network] = None

   class GatewaySummary(DynamicData):
      gatewayType: str
      gatewayId: str

   host: Optional[HostSystem] = None
   hardware: Optional[HardwareSummary] = None
   runtime: Optional[RuntimeInfo] = None
   config: ConfigSummary
   quickStats: QuickStats
   overallStatus: ManagedEntity.Status
   rebootRequired: bool
   customValue: list[CustomFieldsManager.Value] = []
   managementServerIp: Optional[str] = None
   maxEVCModeKey: Optional[str] = None
   currentEVCModeKey: Optional[str] = None
   currentEVCGraphicsModeKey: Optional[str] = None
   gateway: Optional[GatewaySummary] = None
   tpmAttestation: Optional[TpmAttestationInfo] = None
   trustAuthorityAttestationInfos: list[TrustAuthorityAttestationInfo] = []
