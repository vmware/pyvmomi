# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanHostHclInfo

from pyVmomi.vim.vsan import VsanUpdateItem

class VsanClusterHclInfo(DynamicData):
   hclDbLastUpdate: Optional[datetime] = None
   hclDbAgeHealth: Optional[str] = None
   hostResults: list[VsanHostHclInfo] = []
   updateItems: list[VsanUpdateItem] = []
   hclDbAbsent: Optional[bool] = None
