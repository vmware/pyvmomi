# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.VsanHclDeviceConstraint import VsanHclDeviceConstraint

from pyVmomi.vim.vsan.VsanHostDeviceInfo import VsanHostDeviceInfo

class VsanHclReleaseConstraint(DynamicData):
   cluster: ClusterComputeResource
   release: str
   hostDevices: list[VsanHostDeviceInfo] = []
   constraints: list[VsanHclDeviceConstraint] = []
