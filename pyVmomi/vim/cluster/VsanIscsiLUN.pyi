# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.cluster.VsanIscsiLUNCommonInfo import VsanIscsiLUNCommonInfo

from pyVmomi.vim.cluster.VsanObjectInformation import VsanObjectInformation

class VsanIscsiLUN(VsanIscsiLUNCommonInfo):
   targetAlias: str
   uuid: str
   actualSize: long
   objectInformation: Optional[VsanObjectInformation] = None
