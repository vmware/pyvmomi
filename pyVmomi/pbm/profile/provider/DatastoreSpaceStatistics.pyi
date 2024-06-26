# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class DatastoreSpaceStatistics(DynamicData):
   profileId: Optional[str] = None
   physicalTotalInMB: long
   physicalFreeInMB: long
   physicalUsedInMB: long
   logicalLimitInMB: Optional[long] = None
   logicalFreeInMB: long
   logicalUsedInMB: long
