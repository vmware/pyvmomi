# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

class VsanClusterMembershipInfo(DynamicData):
   clusterUuid: Optional[str] = None
   health: Optional[str] = None
   membershipUuid: Optional[str] = None
   memberUuid: list[str] = []
