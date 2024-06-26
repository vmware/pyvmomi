# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VsanHostFwComponent(DynamicData):
   name: str
   url: Optional[str] = None
   sha1sum: Optional[str] = None
   currentVersion: Optional[str] = None
   suggestedVersion: Optional[str] = None
   componentID: list[str] = []
