# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanClusterNetworkPartitionInfo

from pyVmomi.vim.host import VsanNetworkHealthResult
from pyVmomi.vim.host import VsanQueryResultHostInfo

class VsanClusterNetworkHealthResult(DynamicData):
   hostResults: list[VsanNetworkHealthResult] = []
   issueFound: Optional[bool] = None
   vsanVmknicPresent: Optional[bool] = None
   matchingMulticastConfig: Optional[bool] = None
   matchingIpSubnets: Optional[bool] = None
   pingTestSuccess: Optional[bool] = None
   largePingTestSuccess: Optional[bool] = None
   hostLatencyCheckSuccess: Optional[bool] = None
   potentialMulticastIssue: Optional[bool] = None
   otherHostsInVsanCluster: list[str] = []
   partitions: list[VsanClusterNetworkPartitionInfo] = []
   hostsWithVsanDisabled: list[str] = []
   hostsDisconnected: list[str] = []
   hostsCommFailure: list[str] = []
   hostsInEsxMaintenanceMode: list[str] = []
   hostsInVsanMaintenanceMode: list[str] = []
   infoAboutUnexpectedHosts: list[VsanQueryResultHostInfo] = []
   clusterInUnicastMode: Optional[bool] = None
   clusterInRDMAMode: Optional[bool] = None
