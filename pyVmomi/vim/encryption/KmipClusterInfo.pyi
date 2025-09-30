# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.encryption.KeyProviderId import KeyProviderId

from pyVmomi.vim.encryption.KmipServerInfo import KmipServerInfo

class KmipClusterInfo(DynamicData):
   class KmsManagementType(Enum):
      unknown: ClassVar['KmsManagementType'] = 'unknown'
      vCenter: ClassVar['KmsManagementType'] = 'vCenter'
      trustAuthority: ClassVar['KmsManagementType'] = 'trustAuthority'
      nativeProvider: ClassVar['KmsManagementType'] = 'nativeProvider'

   class KeyType(Enum):
      rawKey: ClassVar['KeyType'] = 'rawKey'
      wrappedKey: ClassVar['KeyType'] = 'wrappedKey'

   class KeyInfo(DynamicData):
      pass

   class WrappingKeyIdKeyInfo(KeyInfo):
      keyId: str
      configuredTime: datetime

   class WrappingRotationIntervalKeyInfo(KeyInfo):
      keyId: Optional[str] = None
      rotationInterval: Optional[int] = None
      lastRotation: Optional[datetime] = None

   clusterId: KeyProviderId
   servers: list[KmipServerInfo] = []
   useAsDefault: bool
   managementType: Optional[str] = None
   useAsEntityDefault: list[ManagedEntity] = []
   hasBackup: Optional[bool] = None
   tpmRequired: Optional[bool] = None
   keyId: Optional[str] = None
   defaultKeyType: Optional[str] = None
   keyInfo: Optional[KeyInfo] = None
