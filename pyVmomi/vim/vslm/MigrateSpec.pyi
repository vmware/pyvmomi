# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ServiceLocator

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm import ProfileSpec

from pyVmomi.vim.vslm import CreateSpec
from pyVmomi.vim.vslm import DiskCryptoSpec

class MigrateSpec(DynamicData):
   backingSpec: CreateSpec.BackingSpec
   profile: list[ProfileSpec] = []
   consolidate: Optional[bool] = None
   disksCrypto: Optional[DiskCryptoSpec] = None
   service: Optional[ServiceLocator] = None
