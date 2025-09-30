# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster.SiteFaultDomainConfig import SiteFaultDomainConfig

from pyVmomi.vim.cluster.VsanIscsiTargetServiceConfig import VsanIscsiTargetServiceConfig

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

from pyVmomi.vim.vsan.VsanDatastoreDefaultPolicySelectionConfig import VsanDatastoreDefaultPolicySelectionConfig

from pyVmomi.vim.vsan.VsanDeconvergedNetConfig import VsanDeconvergedNetConfig

from pyVmomi.vim.vsan.VsanEsaConfigInfo import VsanEsaConfigInfo

from pyVmomi.vim.vsan.VsanExtendedConfig import VsanExtendedConfig

from pyVmomi.vim.vsan.VsanHealthConfigSpec import VsanHealthConfigSpec

from pyVmomi.vim.vsan.VsanPMemConfig import VsanPMemConfig

from pyVmomi.vim.vsan.VsanUnmapConfig import VsanUnmapConfig

from pyVmomi.vim.vsan.VsanVumConfig import VsanVumConfig

from pyVmomi.vim.vsan.XVCDatastoreConfig import XVCDatastoreConfig

from pyVmomi.vim.vsan.cluster.ConfigInfo import ConfigInfo

class ConfigInfoEx(ConfigInfo):
   dataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   resyncIopsLimitConfig: Optional[ResyncIopsInfo] = None
   iscsiConfig: Optional[VsanIscsiTargetServiceConfig] = None
   dataEncryptionConfig: Optional[DataEncryptionConfig] = None
   extendedConfig: Optional[VsanExtendedConfig] = None
   datastoreConfig: Optional[DatastoreConfig] = None
   perfsvcConfig: Optional[VsanPerfsvcConfig] = None
   unmapConfig: Optional[VsanUnmapConfig] = None
   vumConfig: Optional[VsanVumConfig] = None
   fileServiceConfig: Optional[FileServiceConfig] = None
   metricsConfig: Optional[MetricsConfig] = None
   rdmaConfig: Optional[RdmaConfig] = None
   dataInTransitEncryptionConfig: Optional[DataInTransitEncryptionConfig] = None
   vsanHealthConfig: Optional[VsanHealthConfigSpec] = None
   mode: Optional[str] = None
   vsanPMemConfig: Optional[VsanPMemConfig] = None
   vsanEsaConfigInfo: Optional[VsanEsaConfigInfo] = None
   xvcDatastoreConfig: Optional[XVCDatastoreConfig] = None
   serverClusterConfig: Optional[VcRemoteVsanServerClusterConfig] = None
   datastoreDefaultPolicySelectionConfig: Optional[VsanDatastoreDefaultPolicySelectionConfig] = None
   snapServiceConfig: Optional[SnapServiceConfig] = None
   deconvergedNetConfig: Optional[VsanDeconvergedNetConfig] = None
   siteFaultDomainConfig: Optional[SiteFaultDomainConfig] = None
