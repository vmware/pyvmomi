# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.Folder import Folder

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.ResourcePool import ResourcePool

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.storageDrs.PodSelectionSpec import PodSelectionSpec

from pyVmomi.vim.vm.CloneSpec import CloneSpec

from pyVmomi.vim.vm.ConfigSpec import ConfigSpec

from pyVmomi.vim.vm.RelocateSpec import RelocateSpec

class StoragePlacementSpec(DynamicData):
   class PlacementType(Enum):
      create: ClassVar['PlacementType'] = 'create'
      reconfigure: ClassVar['PlacementType'] = 'reconfigure'
      relocate: ClassVar['PlacementType'] = 'relocate'
      clone: ClassVar['PlacementType'] = 'clone'

   type: str
   priority: Optional[VirtualMachine.MovePriority] = None
   vm: Optional[VirtualMachine] = None
   podSelectionSpec: PodSelectionSpec
   cloneSpec: Optional[CloneSpec] = None
   cloneName: Optional[str] = None
   configSpec: Optional[ConfigSpec] = None
   relocateSpec: Optional[RelocateSpec] = None
   resourcePool: Optional[ResourcePool] = None
   host: Optional[HostSystem] = None
   folder: Optional[Folder] = None
   disallowPrerequisiteMoves: Optional[bool] = None
   resourceLeaseDurationSec: Optional[int] = None
