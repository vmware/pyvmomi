# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import VasaStorageArray

from pyVmomi.vmodl import DynamicData

class StorageArray(DynamicData):
   class BlockDeviceInterface(Enum):
      fc: ClassVar['BlockDeviceInterface'] = 'fc'
      iscsi: ClassVar['BlockDeviceInterface'] = 'iscsi'
      fcoe: ClassVar['BlockDeviceInterface'] = 'fcoe'
      otherBlock: ClassVar['BlockDeviceInterface'] = 'otherBlock'

   class FileSystemInterface(Enum):
      nfs: ClassVar['FileSystemInterface'] = 'nfs'
      otherFileSystem: ClassVar['FileSystemInterface'] = 'otherFileSystem'

   class VasaProfile(Enum):
      blockDevice: ClassVar['VasaProfile'] = 'blockDevice'
      fileSystem: ClassVar['VasaProfile'] = 'fileSystem'
      capability: ClassVar['VasaProfile'] = 'capability'
      policy: ClassVar['VasaProfile'] = 'policy'
      object: ClassVar['VasaProfile'] = 'object'
      statistics: ClassVar['VasaProfile'] = 'statistics'
      storageDrsBlockDevice: ClassVar['VasaProfile'] = 'storageDrsBlockDevice'
      storageDrsFileSystem: ClassVar['VasaProfile'] = 'storageDrsFileSystem'

   name: str
   uuid: str
   vendorId: str
   modelId: str
   firmware: Optional[str] = None
   alternateName: list[str] = []
   supportedBlockInterface: list[str] = []
   supportedFileSystemInterface: list[str] = []
   supportedProfile: list[str] = []
   priority: Optional[int] = None
   discoverySvc: list[VasaStorageArray.DiscoverySvcInfo] = []
