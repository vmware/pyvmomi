# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.encryption import CryptoKeyId
from pyVmomi.vim.encryption import CryptoKeyPlain
from pyVmomi.vim.encryption import CryptoManager

class CryptoManagerHost(CryptoManager):
   class KeyManagementType(Enum):
      unknown: ClassVar['KeyManagementType'] = 'unknown'
      internal: ClassVar['KeyManagementType'] = 'internal'
      external: ClassVar['KeyManagementType'] = 'external'

   class KeyStatus(DynamicData):
      keyId: CryptoKeyId
      present: bool
      managementType: Optional[str] = None
      accessGranted: Optional[bool] = None

   def Prepare(self) -> NoReturn: ...
   def Enable(self, initialKey: CryptoKeyPlain) -> NoReturn: ...
   def ChangeKey(self, newKey: CryptoKeyPlain) -> Task: ...
   def Disable(self) -> NoReturn: ...
   def GetCryptoKeyStatus(self, keys: list[CryptoKeyId]) -> list[KeyStatus]: ...
