# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanObjectIdentity
from pyVmomi.vim.cluster import VsanObjectSpaceSummary

from pyVmomi.vim.host import VsanObjectOverallHealth

class VsanObjectIdentityAndHealth(DynamicData):
   identities: list[VsanObjectIdentity] = []
   health: Optional[VsanObjectOverallHealth] = None
   spaceSummary: list[VsanObjectSpaceSummary] = []
   rawData: Optional[str] = None
