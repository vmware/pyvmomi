# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import SDDCBase

from pyVmomi.vim.cluster import VsanDiskMappingsConfigSpec
from pyVmomi.vim.cluster import VsanFaultDomainsConfigSpec
from pyVmomi.vim.cluster import VsanIscsiTargetServiceSpec
from pyVmomi.vim.cluster import VsanPerfsvcConfig

from pyVmomi.vim.vsan import DataEfficiencyConfig
from pyVmomi.vim.vsan import DataEncryptionConfig
from pyVmomi.vim.vsan import DataInTransitEncryptionConfig
from pyVmomi.vim.vsan import DatastoreConfig
from pyVmomi.vim.vsan import FileServiceConfig
from pyVmomi.vim.vsan import MetricsConfig
from pyVmomi.vim.vsan import RdmaConfig
from pyVmomi.vim.vsan import ResyncIopsInfo
from pyVmomi.vim.vsan import SnapServiceConfig
from pyVmomi.vim.vsan import VcRemoteVsanServerClusterConfig
from pyVmomi.vim.vsan import VsanEsaConfig
from pyVmomi.vim.vsan import VsanExtendedConfig
from pyVmomi.vim.vsan import VsanHealthConfigSpec
from pyVmomi.vim.vsan import VsanUnmapConfig
from pyVmomi.vim.vsan import VsanVumConfig
from pyVmomi.vim.vsan import XVCDatastoreConfig

from pyVmomi.vim.vsan.cluster import ConfigInfo

class ReconfigSpec(SDDCBase):
   vsanClusterConfig: Optional[ConfigInfo] = None
   dataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   diskMappingSpec: Optional[VsanDiskMappingsConfigSpec] = None
   faultDomainsSpec: Optional[VsanFaultDomainsConfigSpec] = None
   modify: bool
   allowReducedRedundancy: Optional[bool] = None
   resyncIopsLimitConfig: Optional[ResyncIopsInfo] = None
   iscsiSpec: Optional[VsanIscsiTargetServiceSpec] = None
   dataEncryptionConfig: Optional[DataEncryptionConfig] = None
   extendedConfig: Optional[VsanExtendedConfig] = None
   datastoreConfig: Optional[DatastoreConfig] = None
   perfsvcConfig: Optional[VsanPerfsvcConfig] = None
   unmapConfig: Optional[VsanUnmapConfig] = None
   vumConfig: Optional[VsanVumConfig] = None
   metricsConfig: Optional[MetricsConfig] = None
   fileServiceConfig: Optional[FileServiceConfig] = None
   rdmaConfig: Optional[RdmaConfig] = None
   dataInTransitEncryptionConfig: Optional[DataInTransitEncryptionConfig] = None
   mode: Optional[str] = None
   vsanHealthConfig: Optional[VsanHealthConfigSpec] = None
   vsanEsaConfig: Optional[VsanEsaConfig] = None
   xvcDatastoreConfig: Optional[XVCDatastoreConfig] = None
   serverClusterConfig: Optional[VcRemoteVsanServerClusterConfig] = None
   snapServiceConfig: Optional[SnapServiceConfig] = None
