# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore
from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.encryption import CryptoSpec

from pyVmomi.vim.vm import ProfileSpec

class CreateSpec(DynamicData):
   class BackingSpec(DynamicData):
      datastore: Datastore
      path: Optional[str] = None

   class DiskFileBackingSpec(BackingSpec):
      provisioningType: Optional[str] = None

   class RawDiskMappingBackingSpec(BackingSpec):
      lunUuid: str
      compatibilityMode: str

   name: str
   keepAfterDeleteVm: Optional[bool] = None
   backingSpec: BackingSpec
   capacityInMB: long
   profile: list[ProfileSpec] = []
   crypto: Optional[CryptoSpec] = None
   metadata: list[KeyValue] = []
