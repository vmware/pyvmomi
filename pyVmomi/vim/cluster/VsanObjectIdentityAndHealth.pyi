# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanObjectIdentity import VsanObjectIdentity

from pyVmomi.vim.cluster.VsanObjectSpaceSummary import VsanObjectSpaceSummary

from pyVmomi.vim.host.VsanObjectOverallHealth import VsanObjectOverallHealth

class VsanObjectIdentityAndHealth(DynamicData):
   identities: list[VsanObjectIdentity] = []
   health: Optional[VsanObjectOverallHealth] = None
   spaceSummary: list[VsanObjectSpaceSummary] = []
   rawData: Optional[str] = None
