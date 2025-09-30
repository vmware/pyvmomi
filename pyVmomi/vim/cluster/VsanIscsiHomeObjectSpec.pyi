# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanIscsiTargetServiceDefaultConfigSpec import VsanIscsiTargetServiceDefaultConfigSpec

from pyVmomi.vim.vm.ProfileSpec import ProfileSpec

class VsanIscsiHomeObjectSpec(DynamicData):
   storagePolicy: Optional[ProfileSpec] = None
   defaultConfig: Optional[VsanIscsiTargetServiceDefaultConfigSpec] = None
