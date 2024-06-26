# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VibInfo(DynamicData):
   class SoftwareTags(DynamicData):
      tags: list[str] = []

   id: str
   name: str
   version: str
   vendor: str
   summary: str
   softwareTags: Optional[SoftwareTags] = None
   releaseDate: datetime
