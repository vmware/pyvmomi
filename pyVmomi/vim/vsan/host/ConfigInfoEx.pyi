# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vsan import DataEfficiencyConfig
from pyVmomi.vim.vsan import DatastoreConfig
from pyVmomi.vim.vsan import MetricsConfig
from pyVmomi.vim.vsan import RdmaConfig
from pyVmomi.vim.vsan import ResyncIopsInfo
from pyVmomi.vim.vsan import SnapServiceConfig
from pyVmomi.vim.vsan import VsanExtendedConfig
from pyVmomi.vim.vsan import VsanInternalExtendedConfig
from pyVmomi.vim.vsan import VsanUnmapConfig
from pyVmomi.vim.vsan import WitnessHostConfig

from pyVmomi.vim.vsan.host import ConfigInfo
from pyVmomi.vim.vsan.host import DataInTransitEncryptionInfo
from pyVmomi.vim.vsan.host import EncryptionInfo
from pyVmomi.vim.vsan.host import RemoteVsanServerClusterConfig
from pyVmomi.vim.vsan.host import ServerClusterUnicastConfig

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
