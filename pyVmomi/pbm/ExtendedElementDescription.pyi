# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.KeyAnyValue import KeyAnyValue

class ExtendedElementDescription(DynamicData):
   label: str
   summary: str
   key: str
   messageCatalogKeyPrefix: str
   messageArg: list[KeyAnyValue] = []
