# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import OptionValue

from pyVmomi.vim.vm import RelocateSpec

class InstantCloneSpec(DynamicData):
   name: str
   location: RelocateSpec
   config: list[OptionValue] = []
   biosUuid: Optional[str] = None
