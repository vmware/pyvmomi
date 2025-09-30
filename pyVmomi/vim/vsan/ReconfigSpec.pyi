# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.SDDCBase import SDDCBase

from pyVmomi.vim.cluster.VsanDiskMappingsConfigSpec import VsanDiskMappingsConfigSpec

from pyVmomi.vim.cluster.VsanFaultDomainsConfigSpec import VsanFaultDomainsConfigSpec

from pyVmomi.vim.cluster.VsanIscsiTargetServiceSpec import VsanIscsiTargetServiceSpec

from pyVmomi.vim.cluster.VsanPerfsvcConfig import VsanPerfsvcConfig

from pyVmomi.vim.vsan.DataEfficiencyConfig import DataEfficiencyConfig

from pyVmomi.vim.vsan.DataEncryptionConfig import DataEncryptionConfig

from pyVmomi.vim.vsan.DataInTransitEncryptionConfig import DataInTransitEncryptionConfig

from pyVmomi.vim.vsan.DatastoreConfig import DatastoreConfig

from pyVmomi.vim.vsan.FileServiceConfig import FileServiceConfig

from pyVmomi.vim.vsan.MetricsConfig import MetricsConfig

from pyVmomi.vim.vsan.RdmaConfig import RdmaConfig

from pyVmomi.vim.vsan.ResyncIopsInfo import ResyncIopsInfo

from pyVmomi.vim.vsan.SnapServiceConfig import SnapServiceConfig

from pyVmomi.vim.vsan.VcRemoteVsanServerClusterConfig import VcRemoteVsanServerClusterConfig

from pyVmomi.vim.vsan.VsanDeconvergedNetConfig import VsanDeconvergedNetConfig

from pyVmomi.vim.vsan.VsanEsaConfig import VsanEsaConfig

from pyVmomi.vim.vsan.VsanExtendedConfig import VsanExtendedConfig

from pyVmomi.vim.vsan.VsanHealthConfigSpec import VsanHealthConfigSpec

from pyVmomi.vim.vsan.VsanUnmapConfig import VsanUnmapConfig

from pyVmomi.vim.vsan.VsanVumConfig import VsanVumConfig

from pyVmomi.vim.vsan.XVCDatastoreConfig import XVCDatastoreConfig

from pyVmomi.vim.vsan.cluster.ConfigInfo import ConfigInfo

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
   deconvergedNetConfig: Optional[VsanDeconvergedNetConfig] = None
