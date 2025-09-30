# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanStretchedClusterConfig import VsanStretchedClusterConfig

from pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec import AddStoragePoolDiskSpec

from pyVmomi.vim.vsan.host.DiskMapping import DiskMapping

class VsanVcStretchedClusterConfigSpec(DynamicData):
   witnessHost: HostSystem
   clusters: list[VsanStretchedClusterConfig] = []
   witnessDiskMappings: list[DiskMapping] = []
   witnessStoragePoolSpecs: list[AddStoragePoolDiskSpec] = []
