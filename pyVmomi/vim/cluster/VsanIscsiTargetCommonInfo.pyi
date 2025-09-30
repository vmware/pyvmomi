# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster.VsanIscsiTargetAuthSpec import VsanIscsiTargetAuthSpec

from pyVmomi.vim.cluster.VsanIscsiTargetBasicInfo import VsanIscsiTargetBasicInfo

class VsanIscsiTargetCommonInfo(VsanIscsiTargetBasicInfo):
   authSpec: Optional[VsanIscsiTargetAuthSpec] = None
   port: Optional[int] = None
   networkInterface: Optional[str] = None
   affinityLocation: Optional[str] = None
