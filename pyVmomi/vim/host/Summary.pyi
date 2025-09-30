# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long
from pyVmomi.VmomiSupport import short

from pyVmomi.vim.AboutInfo import AboutInfo

from pyVmomi.vim.CustomFieldsManager import CustomFieldsManager

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.Network import Network

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.FeatureVersionInfo import FeatureVersionInfo

from pyVmomi.vim.host.RuntimeInfo import RuntimeInfo

from pyVmomi.vim.host.SystemIdentificationInfo import SystemIdentificationInfo

from pyVmomi.vim.host.TpmAttestationInfo import TpmAttestationInfo

from pyVmomi.vim.host.TrustAuthorityAttestationInfo import TrustAuthorityAttestationInfo

class Summary(DynamicData):
   class HardwareSummary(DynamicData):
      vendor: str
      model: str
      family: Optional[str] = None
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
      sslCertificate: Optional[str] = None
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
