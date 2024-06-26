# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import Datastore
from pyVmomi.vim import HostSystem
from pyVmomi.vim import StoragePod
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import RuleInfo

from pyVmomi.vim.vm import CloneSpec
from pyVmomi.vim.vm import ConfigSpec
from pyVmomi.vim.vm import RelocateSpec

class PlacementSpec(DynamicData):
   class PlacementType(Enum):
      create: ClassVar['PlacementType'] = 'create'
      reconfigure: ClassVar['PlacementType'] = 'reconfigure'
      relocate: ClassVar['PlacementType'] = 'relocate'
      clone: ClassVar['PlacementType'] = 'clone'

   priority: Optional[VirtualMachine.MovePriority] = None
   vm: Optional[VirtualMachine] = None
   configSpec: Optional[ConfigSpec] = None
   relocateSpec: Optional[RelocateSpec] = None
   hosts: list[HostSystem] = []
   datastores: list[Datastore] = []
   storagePods: list[StoragePod] = []
   disallowPrerequisiteMoves: Optional[bool] = None
   rules: list[RuleInfo] = []
   key: Optional[str] = None
   placementType: Optional[str] = None
   cloneSpec: Optional[CloneSpec] = None
   cloneName: Optional[str] = None
