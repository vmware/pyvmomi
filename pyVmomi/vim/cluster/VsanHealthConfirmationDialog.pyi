# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VsanHealthConfirmationDialog(DynamicData):
   title: str
   subTitle: Optional[str] = None
   content: str
   agreeLabel: Optional[str] = None
   closeLabel: Optional[str] = None
   isWarning: Optional[bool] = None
