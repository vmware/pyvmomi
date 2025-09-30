# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.profile.ApplyProfileProperty import ApplyProfileProperty

from pyVmomi.vim.profile.Policy import Policy

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
