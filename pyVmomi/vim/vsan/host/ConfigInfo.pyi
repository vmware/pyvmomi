# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.host.DiskMapInfo import DiskMapInfo

from pyVmomi.vim.vsan.host.DiskMapping import DiskMapping

from pyVmomi.vim.vsan.host.IpConfig import IpConfig

class ConfigInfo(DynamicData):
   class StorageInfo(DynamicData):
      autoClaimStorage: Optional[bool] = None
      diskMapping: list[DiskMapping] = []
      diskMapInfo: list[DiskMapInfo] = []
      checksumEnabled: Optional[bool] = None

   class ClusterInfo(DynamicData):
      uuid: Optional[str] = None
      nodeUuid: Optional[str] = None

   class NetworkInfo(DynamicData):
      class PortConfig(DynamicData):
         ipConfig: Optional[IpConfig] = None
         device: str

      port: list[PortConfig] = []

   class FaultDomainInfo(DynamicData):
      name: str

   enabled: Optional[bool] = None
   hostSystem: Optional[HostSystem] = None
   clusterInfo: Optional[ClusterInfo] = None
   storageInfo: Optional[StorageInfo] = None
   networkInfo: Optional[NetworkInfo] = None
   faultDomainInfo: Optional[FaultDomainInfo] = None
   vsanEsaEnabled: Optional[bool] = None
