# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import SharesInfo
from pyVmomi.vim import StorageResourceManager

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.encryption import CryptoKeyId

from pyVmomi.vim.vm import BaseIndependentFilterSpec

from pyVmomi.vim.vslm import ID

from pyVmomi.vim.vm.device import VirtualDevice

class VirtualDisk(VirtualDevice):
   class DeltaDiskFormat(Enum):
      redoLogFormat: ClassVar['DeltaDiskFormat'] = 'redoLogFormat'
      nativeFormat: ClassVar['DeltaDiskFormat'] = 'nativeFormat'
      seSparseFormat: ClassVar['DeltaDiskFormat'] = 'seSparseFormat'

   class DeltaDiskFormatVariant(Enum):
      vmfsSparseVariant: ClassVar['DeltaDiskFormatVariant'] = 'vmfsSparseVariant'
      vsanSparseVariant: ClassVar['DeltaDiskFormatVariant'] = 'vsanSparseVariant'

   class Sharing(Enum):
      sharingNone: ClassVar['Sharing'] = 'sharingNone'
      sharingMultiWriter: ClassVar['Sharing'] = 'sharingMultiWriter'

   class SparseVer1BackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      split: Optional[bool] = None
      writeThrough: Optional[bool] = None
      spaceUsedInKB: Optional[long] = None
      contentId: Optional[str] = None
      parent: Optional[SparseVer1BackingInfo] = None

   class SparseVer2BackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      split: Optional[bool] = None
      writeThrough: Optional[bool] = None
      spaceUsedInKB: Optional[long] = None
      uuid: Optional[str] = None
      contentId: Optional[str] = None
      changeId: Optional[str] = None
      parent: Optional[SparseVer2BackingInfo] = None
      keyId: Optional[CryptoKeyId] = None

   class FlatVer1BackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      split: Optional[bool] = None
      writeThrough: Optional[bool] = None
      contentId: Optional[str] = None
      parent: Optional[FlatVer1BackingInfo] = None

   class FlatVer2BackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      split: Optional[bool] = None
      writeThrough: Optional[bool] = None
      thinProvisioned: Optional[bool] = None
      eagerlyScrub: Optional[bool] = None
      uuid: Optional[str] = None
      contentId: Optional[str] = None
      changeId: Optional[str] = None
      parent: Optional[FlatVer2BackingInfo] = None
      deltaDiskFormat: Optional[str] = None
      digestEnabled: Optional[bool] = None
      deltaGrainSize: Optional[int] = None
      deltaDiskFormatVariant: Optional[str] = None
      sharing: Optional[str] = None
      keyId: Optional[CryptoKeyId] = None

   class SeSparseBackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      writeThrough: Optional[bool] = None
      uuid: Optional[str] = None
      contentId: Optional[str] = None
      changeId: Optional[str] = None
      parent: Optional[SeSparseBackingInfo] = None
      deltaDiskFormat: Optional[str] = None
      digestEnabled: Optional[bool] = None
      grainSize: Optional[int] = None
      keyId: Optional[CryptoKeyId] = None

   class RawDiskVer2BackingInfo(VirtualDevice.DeviceBackingInfo):
      descriptorFileName: str
      uuid: Optional[str] = None
      changeId: Optional[str] = None
      sharing: Optional[str] = None

   class PartitionedRawDiskVer2BackingInfo(RawDiskVer2BackingInfo):
      partition: list[int] = []

   class RawDiskMappingVer1BackingInfo(VirtualDevice.FileBackingInfo):
      lunUuid: Optional[str] = None
      deviceName: Optional[str] = None
      compatibilityMode: Optional[str] = None
      diskMode: Optional[str] = None
      uuid: Optional[str] = None
      contentId: Optional[str] = None
      changeId: Optional[str] = None
      parent: Optional[RawDiskMappingVer1BackingInfo] = None
      deltaDiskFormat: Optional[str] = None
      deltaGrainSize: Optional[int] = None
      sharing: Optional[str] = None

   class LocalPMemBackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      uuid: Optional[str] = None
      volumeUUID: Optional[str] = None
      contentId: Optional[str] = None

   class VFlashCacheConfigInfo(DynamicData):
      class CacheConsistencyType(Enum):
         strong: ClassVar['CacheConsistencyType'] = 'strong'
         weak: ClassVar['CacheConsistencyType'] = 'weak'

      class CacheMode(Enum):
         write_thru: ClassVar['CacheMode'] = 'write_thru'
         write_back: ClassVar['CacheMode'] = 'write_back'

      vFlashModule: Optional[str] = None
      reservationInMB: Optional[long] = None
      cacheConsistencyType: Optional[str] = None
      cacheMode: Optional[str] = None
      blockSizeInKB: Optional[long] = None

   capacityInKB: long
   capacityInBytes: Optional[long] = None
   shares: Optional[SharesInfo] = None
   storageIOAllocation: Optional[StorageResourceManager.IOAllocationInfo] = None
   diskObjectId: Optional[str] = None
   vFlashCacheConfigInfo: Optional[VFlashCacheConfigInfo] = None
   iofilter: list[str] = []
   vDiskId: Optional[ID] = None
   vDiskVersion: Optional[int] = None
   nativeUnmanagedLinkedClone: Optional[bool] = None
   independentFilters: list[BaseIndependentFilterSpec] = []
   guestReadOnly: Optional[bool] = None
