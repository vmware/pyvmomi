# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.VsanComparator import VsanComparator

from pyVmomi.vmodl.DynamicData import DynamicData

class VsanJsonFilterRule(DynamicData):
   filterComparator: Optional[VsanComparator] = None
   comparablePath: list[str] = []
   keysWithStrVal: list[str] = []
   propertyName: Optional[str] = None
