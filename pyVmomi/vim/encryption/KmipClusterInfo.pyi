# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.encryption import KeyProviderId
from pyVmomi.vim.encryption import KmipServerInfo

class KmipClusterInfo(DynamicData):
   class KmsManagementType(Enum):
      unknown: ClassVar['KmsManagementType'] = 'unknown'
      vCenter: ClassVar['KmsManagementType'] = 'vCenter'
      trustAuthority: ClassVar['KmsManagementType'] = 'trustAuthority'
      nativeProvider: ClassVar['KmsManagementType'] = 'nativeProvider'

   clusterId: KeyProviderId
   servers: list[KmipServerInfo] = []
   useAsDefault: bool
   managementType: Optional[str] = None
   useAsEntityDefault: list[ManagedEntity] = []
   hasBackup: Optional[bool] = None
   tpmRequired: Optional[bool] = None
   keyId: Optional[str] = None
