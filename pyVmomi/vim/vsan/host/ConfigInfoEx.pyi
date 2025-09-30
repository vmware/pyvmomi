# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vsan.DataEfficiencyConfig import DataEfficiencyConfig

from pyVmomi.vim.vsan.DatastoreConfig import DatastoreConfig

from pyVmomi.vim.vsan.MetricsConfig import MetricsConfig

from pyVmomi.vim.vsan.RdmaConfig import RdmaConfig

from pyVmomi.vim.vsan.ResyncIopsInfo import ResyncIopsInfo

from pyVmomi.vim.vsan.SnapServiceConfig import SnapServiceConfig

from pyVmomi.vim.vsan.VsanDeconvergedNetConfig import VsanDeconvergedNetConfig

from pyVmomi.vim.vsan.VsanExtendedConfig import VsanExtendedConfig

from pyVmomi.vim.vsan.VsanInternalExtendedConfig import VsanInternalExtendedConfig

from pyVmomi.vim.vsan.VsanUnmapConfig import VsanUnmapConfig

from pyVmomi.vim.vsan.WitnessHostConfig import WitnessHostConfig

from pyVmomi.vim.vsan.host.ConfigInfo import ConfigInfo

from pyVmomi.vim.vsan.host.DataInTransitEncryptionInfo import DataInTransitEncryptionInfo

from pyVmomi.vim.vsan.host.EncryptionInfo import EncryptionInfo

from pyVmomi.vim.vsan.host.RemoteVsanServerClusterConfig import RemoteVsanServerClusterConfig

from pyVmomi.vim.vsan.host.ServerClusterUnicastConfig import ServerClusterUnicastConfig

class ConfigInfoEx(ConfigInfo):
   encryptionInfo: Optional[EncryptionInfo] = None
   dataEfficiencyInfo: Optional[DataEfficiencyConfig] = None
   resyncIopsLimitInfo: Optional[ResyncIopsInfo] = None
   extendedConfig: Optional[VsanExtendedConfig] = None
   datastoreInfo: Optional[DatastoreConfig] = None
   unmapConfig: Optional[VsanUnmapConfig] = None
   witnessHostConfig: list[WitnessHostConfig] = []
   internalExtendedConfig: Optional[VsanInternalExtendedConfig] = None
   metricsConfig: Optional[MetricsConfig] = None
   unicastConfig: Optional[ServerClusterUnicastConfig] = None
   rdmaConfig: Optional[RdmaConfig] = None
   dataInTransitEncryptionInfo: Optional[DataInTransitEncryptionInfo] = None
   mode: Optional[str] = None
   serverClusterConfigs: list[RemoteVsanServerClusterConfig] = []
   snapServiceConfig: Optional[SnapServiceConfig] = None
   deconvergedNetConfig: Optional[VsanDeconvergedNetConfig] = None
