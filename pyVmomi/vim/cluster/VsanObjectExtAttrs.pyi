# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

class VsanObjectExtAttrs(DynamicData):
   uuid: str
   objectType: Optional[str] = None
   objectPath: Optional[str] = None
   groupUuid: Optional[str] = None
   directoryName: Optional[str] = None
