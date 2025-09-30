# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.StoragePod import StoragePod

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.RuleInfo import RuleInfo

from pyVmomi.vim.vm.CloneSpec import CloneSpec

from pyVmomi.vim.vm.ConfigSpec import ConfigSpec

from pyVmomi.vim.vm.RelocateSpec import RelocateSpec

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
