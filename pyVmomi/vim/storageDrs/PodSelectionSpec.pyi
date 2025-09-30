# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.StoragePod import StoragePod

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.RuleInfo import RuleInfo

from pyVmomi.vim.storageDrs.VmConfigInfo import VmConfigInfo

from pyVmomi.vim.vm.ProfileSpec import ProfileSpec

from pyVmomi.vim.vm.device.VirtualDevice import VirtualDevice

class PodSelectionSpec(DynamicData):
   class VmPodConfig(DynamicData):
      storagePod: StoragePod
      disk: list[DiskLocator] = []
      vmConfig: Optional[VmConfigInfo] = None
      interVmRule: list[RuleInfo] = []

   class DiskLocator(DynamicData):
      diskId: int
      diskMoveType: Optional[str] = None
      diskBackingInfo: Optional[VirtualDevice.BackingInfo] = None
      profile: list[ProfileSpec] = []

   initialVmConfig: list[VmPodConfig] = []
   storagePod: Optional[StoragePod] = None
