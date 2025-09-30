# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster.VsanIscsiTargetCommonInfo import VsanIscsiTargetCommonInfo

from pyVmomi.vim.cluster.VsanObjectInformation import VsanObjectInformation

class VsanIscsiTarget(VsanIscsiTargetCommonInfo):
   lunCount: Optional[int] = None
   objectInformation: Optional[VsanObjectInformation] = None
   ioOwnerHost: Optional[str] = None
   initiators: list[str] = []
   initiatorGroups: list[str] = []
