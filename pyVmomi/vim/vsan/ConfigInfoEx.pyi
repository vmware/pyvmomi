# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster import VsanIscsiTargetServiceConfig
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
from pyVmomi.vim.vsan import VsanDatastoreDefaultPolicySelectionConfig
from pyVmomi.vim.vsan import VsanEsaConfigInfo
from pyVmomi.vim.vsan import VsanExtendedConfig
from pyVmomi.vim.vsan import VsanHealthConfigSpec
from pyVmomi.vim.vsan import VsanPMemConfig
from pyVmomi.vim.vsan import VsanUnmapConfig
from pyVmomi.vim.vsan import VsanVumConfig
from pyVmomi.vim.vsan import XVCDatastoreConfig

from pyVmomi.vim.vsan.cluster import ConfigInfo

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
