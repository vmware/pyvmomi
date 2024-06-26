# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import XvcQueryFilter

class XvcQuerySpec(DynamicData):
   objectModel: Optional[str] = None
   properties: list[str] = []
   filter: Optional[XvcQueryFilter] = None
   offset: Optional[int] = None
   limit: Optional[int] = None
   returnTotalCount: Optional[bool] = None
