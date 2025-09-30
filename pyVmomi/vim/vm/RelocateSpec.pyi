# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.Folder import Folder

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.ResourcePool import ResourcePool

from pyVmomi.vim.ServiceLocator import ServiceLocator

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.encryption.CryptoSpec import CryptoSpec

from pyVmomi.vim.vm.BaseIndependentFilterSpec import BaseIndependentFilterSpec

from pyVmomi.vim.vm.ProfileSpec import ProfileSpec

from pyVmomi.vim.vm.device.VirtualDevice import VirtualDevice

from pyVmomi.vim.vm.device.VirtualDeviceSpec import VirtualDeviceSpec

class RelocateSpec(DynamicData):
   class Transformation(Enum):
      flat: ClassVar['Transformation'] = 'flat'
      sparse: ClassVar['Transformation'] = 'sparse'

   class DiskLocator(DynamicData):
      class BackingSpec(DynamicData):
         parent: Optional[BackingSpec] = None
         crypto: Optional[CryptoSpec] = None

      diskId: int
      datastore: Datastore
      diskMoveType: Optional[str] = None
      diskBackingInfo: Optional[VirtualDevice.BackingInfo] = None
      profile: list[ProfileSpec] = []
      backing: Optional[BackingSpec] = None
      filterSpec: list[BaseIndependentFilterSpec] = []

   class DiskMoveOptions(Enum):
      moveAllDiskBackingsAndAllowSharing: ClassVar['DiskMoveOptions'] = 'moveAllDiskBackingsAndAllowSharing'
      moveAllDiskBackingsAndDisallowSharing: ClassVar['DiskMoveOptions'] = 'moveAllDiskBackingsAndDisallowSharing'
      moveChildMostDiskBacking: ClassVar['DiskMoveOptions'] = 'moveChildMostDiskBacking'
      createNewChildDiskBacking: ClassVar['DiskMoveOptions'] = 'createNewChildDiskBacking'
      moveAllDiskBackingsAndConsolidate: ClassVar['DiskMoveOptions'] = 'moveAllDiskBackingsAndConsolidate'

   service: Optional[ServiceLocator] = None
   folder: Optional[Folder] = None
   datastore: Optional[Datastore] = None
   diskMoveType: Optional[str] = None
   pool: Optional[ResourcePool] = None
   host: Optional[HostSystem] = None
   disk: list[DiskLocator] = []
   transform: Optional[Transformation] = None
   deviceChange: list[VirtualDeviceSpec] = []
   profile: list[ProfileSpec] = []
   cryptoSpec: Optional[CryptoSpec] = None
