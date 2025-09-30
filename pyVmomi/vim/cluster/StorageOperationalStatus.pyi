# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

class StorageOperationalStatus(DynamicData):
   healthy: Optional[bool] = None
   operationETA: Optional[datetime] = None
   operationProgress: Optional[long] = None
   transitional: Optional[bool] = None
