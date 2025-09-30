# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Description import Description

from pyVmomi.vmodl.KeyAnyValue import KeyAnyValue

class ExtendedDescription(Description):
   messageCatalogKeyPrefix: str
   messageArg: list[KeyAnyValue] = []
