# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.encryption import CryptoKeyId
from pyVmomi.vim.encryption import CryptoKeyPlain
from pyVmomi.vim.encryption import CryptoKeyResult

class CryptoManager(ManagedObject):
   @property
   def enabled(self) -> bool: ...

   def AddKey(self, key: CryptoKeyPlain) -> NoReturn: ...
   def AddKeys(self, keys: list[CryptoKeyPlain]) -> list[CryptoKeyResult]: ...
   def RemoveKey(self, key: CryptoKeyId, force: bool) -> NoReturn: ...
   def RemoveKeys(self, keys: list[CryptoKeyId], force: bool) -> list[CryptoKeyResult]: ...
   def ListKeys(self, limit: Optional[int]) -> list[CryptoKeyId]: ...
