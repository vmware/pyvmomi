# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import StoragePod

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import RuleInfo

from pyVmomi.vim.storageDrs import VmConfigInfo

from pyVmomi.vim.vm import ProfileSpec

from pyVmomi.vim.vm.device import VirtualDevice

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
