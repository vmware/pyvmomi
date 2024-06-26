# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster import VsanIscsiTargetCommonInfo

from pyVmomi.vim.vm import ProfileSpec

class VsanIscsiTargetSpec(VsanIscsiTargetCommonInfo):
   storagePolicy: Optional[ProfileSpec] = None
   newAlias: Optional[str] = None
