# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.encryption.CryptoKeyId import CryptoKeyId

from pyVmomi.vim.encryption.CryptoKeyPlain import CryptoKeyPlain

from pyVmomi.vim.encryption.CryptoManager import CryptoManager

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

   def Prepare(self) -> None: ...
   def Enable(self, initialKey: CryptoKeyPlain) -> None: ...
   def ChangeKey(self, newKey: CryptoKeyPlain) -> Task: ...
   def Disable(self) -> None: ...
   def GetCryptoKeyStatus(self, keys: list[CryptoKeyId]) -> list[KeyStatus]: ...
