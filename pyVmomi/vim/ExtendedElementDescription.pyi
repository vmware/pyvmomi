# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ElementDescription import ElementDescription

from pyVmomi.vmodl.KeyAnyValue import KeyAnyValue

class ExtendedElementDescription(ElementDescription):
   messageCatalogKeyPrefix: str
   messageArg: list[KeyAnyValue] = []
