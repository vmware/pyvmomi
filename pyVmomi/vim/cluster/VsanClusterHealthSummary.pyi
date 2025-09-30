# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanClusterAdvCfgSyncResult import VsanClusterAdvCfgSyncResult

from pyVmomi.vim.cluster.VsanClusterBalanceSummary import VsanClusterBalanceSummary

from pyVmomi.vim.cluster.VsanClusterClomdLivenessResult import VsanClusterClomdLivenessResult

from pyVmomi.vim.cluster.VsanClusterDitEncryptionHealthSummary import VsanClusterDitEncryptionHealthSummary

from pyVmomi.vim.cluster.VsanClusterEncryptionHealthSummary import VsanClusterEncryptionHealthSummary

from pyVmomi.vim.cluster.VsanClusterFileServiceHealthSummary import VsanClusterFileServiceHealthSummary

from pyVmomi.vim.cluster.VsanClusterGlobalDedupHealthSummary import VsanClusterGlobalDedupHealthSummary

from pyVmomi.vim.cluster.VsanClusterHclInfo import VsanClusterHclInfo

from pyVmomi.vim.cluster.VsanClusterHealthGroup import VsanClusterHealthGroup

from pyVmomi.vim.cluster.VsanClusterHealthSystemStatusResult import VsanClusterHealthSystemStatusResult

from pyVmomi.vim.cluster.VsanClusterHealthSystemVersionResult import VsanClusterHealthSystemVersionResult

from pyVmomi.vim.cluster.VsanClusterLimitHealthResult import VsanClusterLimitHealthResult

from pyVmomi.vim.cluster.VsanClusterNetworkHealthResult import VsanClusterNetworkHealthResult

from pyVmomi.vim.cluster.VsanClusterVMsHealthOverallResult import VsanClusterVMsHealthOverallResult

from pyVmomi.vim.cluster.VsanHostCreateVmHealthTestResult import VsanHostCreateVmHealthTestResult

from pyVmomi.vim.host.VsanObjectOverallHealth import VsanObjectOverallHealth

from pyVmomi.vim.host.VsanPhysicalDiskHealthSummary import VsanPhysicalDiskHealthSummary

from pyVmomi.vim.vsan.VsanBurnInTestCheckResult import VsanBurnInTestCheckResult

from pyVmomi.vim.vsan.VsanConfigCheckResult import VsanConfigCheckResult

from pyVmomi.vim.vsan.VsanGenericClusterBestPracticeHealth import VsanGenericClusterBestPracticeHealth

from pyVmomi.vim.vsan.VsanNetworkConfigBestPracticeHealth import VsanNetworkConfigBestPracticeHealth

from pyVmomi.vim.vsan.VsanPerfsvcHealthResult import VsanPerfsvcHealthResult

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
   globalDedupHealth: Optional[VsanClusterGlobalDedupHealthSummary] = None
