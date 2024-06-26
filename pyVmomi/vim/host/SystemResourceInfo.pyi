# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ResourceConfigSpec

from pyVmomi.vmodl import DynamicData

class SystemResourceInfo(DynamicData):
   key: str
   config: Optional[ResourceConfigSpec] = None
   child: list[SystemResourceInfo] = []
