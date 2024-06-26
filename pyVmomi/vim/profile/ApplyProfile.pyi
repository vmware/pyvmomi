# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.profile import ApplyProfileProperty
from pyVmomi.vim.profile import Policy

class ApplyProfile(DynamicData):
   enabled: bool
   policy: list[Policy] = []
   profileTypeName: Optional[str] = None
   profileVersion: Optional[str] = None
   property: list[ApplyProfileProperty] = []
   favorite: Optional[bool] = None
   toBeMerged: Optional[bool] = None
   toReplaceWith: Optional[bool] = None
   toBeDeleted: Optional[bool] = None
   copyEnableStatus: Optional[bool] = None
   hidden: Optional[bool] = None
