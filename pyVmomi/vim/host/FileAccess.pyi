# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class FileAccess(DynamicData):
   class Modes(DynamicData):
      browse: Optional[str] = None
      read: str
      modify: str
      use: str
      admin: Optional[str] = None
      full: str

   who: str
   what: str
