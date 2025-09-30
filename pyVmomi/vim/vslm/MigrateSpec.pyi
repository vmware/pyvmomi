# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ServiceLocator import ServiceLocator

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vm.ProfileSpec import ProfileSpec

from pyVmomi.vim.vslm.CreateSpec import CreateSpec

from pyVmomi.vim.vslm.DiskCryptoSpec import DiskCryptoSpec

class MigrateSpec(DynamicData):
   backingSpec: CreateSpec.BackingSpec
   profile: list[ProfileSpec] = []
   consolidate: Optional[bool] = None
   disksCrypto: Optional[DiskCryptoSpec] = None
   service: Optional[ServiceLocator] = None
