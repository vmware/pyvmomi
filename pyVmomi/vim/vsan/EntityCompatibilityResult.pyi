# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.KeyAnyValue import KeyAnyValue

from pyVmomi.vmodl.LocalizableMessage import LocalizableMessage

class EntityCompatibilityResult(DynamicData):
   entity: ManagedEntity
   compatible: bool
   incompatibleReasons: list[LocalizableMessage] = []
   extendedAttributes: list[KeyAnyValue] = []
