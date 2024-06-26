# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import StorageResourceManager

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import BoolOption
from pyVmomi.vim.option import ChoiceOption
from pyVmomi.vim.option import LongOption

from pyVmomi.vim.vm.device import VirtualDeviceOption

class VirtualDiskOption(VirtualDeviceOption):
   class DiskMode(Enum):
      persistent: ClassVar['DiskMode'] = 'persistent'
      nonpersistent: ClassVar['DiskMode'] = 'nonpersistent'
      undoable: ClassVar['DiskMode'] = 'undoable'
      independent_persistent: ClassVar['DiskMode'] = 'independent_persistent'
      independent_nonpersistent: ClassVar['DiskMode'] = 'independent_nonpersistent'
      append: ClassVar['DiskMode'] = 'append'

   class CompatibilityMode(Enum):
      virtualMode: ClassVar['CompatibilityMode'] = 'virtualMode'
      physicalMode: ClassVar['CompatibilityMode'] = 'physicalMode'

   class SparseVer1BackingOption(VirtualDeviceOption.FileBackingOption):
      diskModes: ChoiceOption
      split: BoolOption
      writeThrough: BoolOption
      growable: bool

   class SparseVer2BackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: ChoiceOption
      split: BoolOption
      writeThrough: BoolOption
      growable: bool
      hotGrowable: bool
      uuid: bool

   class FlatVer1BackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: ChoiceOption
      split: BoolOption
      writeThrough: BoolOption
      growable: bool

   class DeltaDiskFormatsSupported(DynamicData):
      datastoreType: type
      deltaDiskFormat: ChoiceOption

   class FlatVer2BackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: ChoiceOption
      split: BoolOption
      writeThrough: BoolOption
      growable: bool
      hotGrowable: bool
      uuid: bool
      thinProvisioned: BoolOption
      eagerlyScrub: BoolOption
      deltaDiskFormat: ChoiceOption
      deltaDiskFormatsSupported: list[DeltaDiskFormatsSupported] = []

   class SeSparseBackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: ChoiceOption
      writeThrough: BoolOption
      growable: bool
      hotGrowable: bool
      uuid: bool
      deltaDiskFormatsSupported: list[DeltaDiskFormatsSupported] = []

   class RawDiskVer2BackingOption(VirtualDeviceOption.DeviceBackingOption):
      descriptorFileNameExtensions: ChoiceOption
      uuid: bool

   class PartitionedRawDiskVer2BackingOption(RawDiskVer2BackingOption):
      pass

   class RawDiskMappingVer1BackingOption(VirtualDeviceOption.DeviceBackingOption):
      descriptorFileNameExtensions: Optional[ChoiceOption] = None
      compatibilityMode: ChoiceOption
      diskMode: ChoiceOption
      uuid: bool

   class LocalPMemBackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: ChoiceOption
      growable: bool
      hotGrowable: bool
      uuid: bool

   class VFlashCacheConfigOption(DynamicData):
      cacheConsistencyType: ChoiceOption
      cacheMode: ChoiceOption
      reservationInMB: LongOption
      blockSizeInKB: LongOption

   capacityInKB: LongOption
   ioAllocationOption: StorageResourceManager.IOAllocationOption
   vFlashCacheConfigOption: Optional[VFlashCacheConfigOption] = None
