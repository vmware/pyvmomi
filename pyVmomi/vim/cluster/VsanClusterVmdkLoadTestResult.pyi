# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanClusterProactiveTestResult import VsanClusterProactiveTestResult

from pyVmomi.vim.host.VsanHostVmdkLoadTestResult import VsanHostVmdkLoadTestResult

class VsanClusterVmdkLoadTestResult(DynamicData):
   task: Optional[Task] = None
   clusterResult: Optional[VsanClusterProactiveTestResult] = None
   hostResults: list[VsanHostVmdkLoadTestResult] = []
