# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.encryption.KeyProviderId import KeyProviderId

from pyVmomi.vim.encryption.KmipServerInfo import KmipServerInfo

class KmipServerSpec(DynamicData):
   class KeySpec(DynamicData):
      pass

   class WrappingKeyIdKeySpec(KeySpec):
      keyId: str

   class WrappingRotationIntervalKeySpec(KeySpec):
      rotationInterval: Optional[int] = None

   clusterId: KeyProviderId
   info: KmipServerInfo
   password: Optional[str] = None
   defaultKeyType: Optional[str] = None
   keySpec: Optional[KeySpec] = None
