# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vim import ClusterComputeResource

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanClusterAdvCfgSyncResult
from pyVmomi.vim.cluster import VsanClusterBalanceSummary
from pyVmomi.vim.cluster import VsanClusterClomdLivenessResult
from pyVmomi.vim.cluster import VsanClusterDitEncryptionHealthSummary
from pyVmomi.vim.cluster import VsanClusterEncryptionHealthSummary
from pyVmomi.vim.cluster import VsanClusterFileServiceHealthSummary
from pyVmomi.vim.cluster import VsanClusterHclInfo
from pyVmomi.vim.cluster import VsanClusterHealthGroup
from pyVmomi.vim.cluster import VsanClusterHealthSystemStatusResult
from pyVmomi.vim.cluster import VsanClusterHealthSystemVersionResult
from pyVmomi.vim.cluster import VsanClusterLimitHealthResult
from pyVmomi.vim.cluster import VsanClusterNetworkHealthResult
from pyVmomi.vim.cluster import VsanClusterVMsHealthOverallResult
from pyVmomi.vim.cluster import VsanHostCreateVmHealthTestResult

from pyVmomi.vim.host import VsanObjectOverallHealth
from pyVmomi.vim.host import VsanPhysicalDiskHealthSummary

from pyVmomi.vim.vsan import VsanBurnInTestCheckResult
from pyVmomi.vim.vsan import VsanConfigCheckResult
from pyVmomi.vim.vsan import VsanGenericClusterBestPracticeHealth
from pyVmomi.vim.vsan import VsanNetworkConfigBestPracticeHealth
from pyVmomi.vim.vsan import VsanPerfsvcHealthResult

class VsanClusterHealthSummary(DynamicData):
   clusterStatus: Optional[VsanClusterHealthSystemStatusResult] = None
   timestamp: Optional[datetime] = None
   clusterVersions: Optional[VsanClusterHealthSystemVersionResult] = None
   objectHealth: Optional[VsanObjectOverallHealth] = None
   vmHealth: Optional[VsanClusterVMsHealthOverallResult] = None
   networkHealth: Optional[VsanClusterNetworkHealthResult] = None
   limitHealth: Optional[VsanClusterLimitHealthResult] = None
   advCfgSync: list[VsanClusterAdvCfgSyncResult] = []
   createVmHealth: list[VsanHostCreateVmHealthTestResult] = []
   physicalDisksHealth: list[VsanPhysicalDiskHealthSummary] = []
   encryptionHealth: Optional[VsanClusterEncryptionHealthSummary] = None
   hclInfo: Optional[VsanClusterHclInfo] = None
   groups: list[VsanClusterHealthGroup] = []
   overallHealth: str
   overallHealthDescription: str
   clomdLiveness: Optional[VsanClusterClomdLivenessResult] = None
   diskBalance: Optional[VsanClusterBalanceSummary] = None
   genericCluster: Optional[VsanGenericClusterBestPracticeHealth] = None
   networkConfig: Optional[VsanNetworkConfigBestPracticeHealth] = None
   vsanConfig: Optional[VsanConfigCheckResult] = None
   burnInTest: Optional[VsanBurnInTestCheckResult] = None
   perfsvcHealth: Optional[VsanPerfsvcHealthResult] = None
   cluster: Optional[ClusterComputeResource] = None
   fileServiceHealth: Optional[VsanClusterFileServiceHealthSummary] = None
   ditEncryptionHealth: Optional[VsanClusterDitEncryptionHealthSummary] = None
   healthScore: Optional[int] = None
