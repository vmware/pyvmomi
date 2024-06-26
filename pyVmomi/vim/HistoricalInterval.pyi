# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class HistoricalInterval(DynamicData):
   key: int
   samplingPeriod: int
   name: str
   length: int
   level: Optional[int] = None
   enabled: bool
