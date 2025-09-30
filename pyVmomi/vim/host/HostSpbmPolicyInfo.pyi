# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.HostSpbmPolicyBlobInfo import HostSpbmPolicyBlobInfo

class HostSpbmPolicyInfo(DynamicData):
   profileId: str
   name: str
   description: Optional[str] = None
   generationId: long
   policyBlobInfo: list[HostSpbmPolicyBlobInfo] = []
