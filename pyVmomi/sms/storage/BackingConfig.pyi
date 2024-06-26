# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class BackingConfig(DynamicData):
   thinProvisionBackingIdentifier: Optional[str] = None
   deduplicationBackingIdentifier: Optional[str] = None
   autoTieringEnabled: Optional[bool] = None
   deduplicationEfficiency: Optional[long] = None
   performanceOptimizationInterval: Optional[long] = None
