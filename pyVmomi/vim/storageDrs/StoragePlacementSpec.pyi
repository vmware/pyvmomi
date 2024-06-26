# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import Folder
from pyVmomi.vim import HostSystem
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.storageDrs import PodSelectionSpec

from pyVmomi.vim.vm import CloneSpec
from pyVmomi.vim.vm import ConfigSpec
from pyVmomi.vim.vm import RelocateSpec

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
