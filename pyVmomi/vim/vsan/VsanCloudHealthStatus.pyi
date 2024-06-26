# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VsanCloudHealthStatus(DynamicData):
   collectorRunning: Optional[bool] = None
   lastSentTimestamp: Optional[str] = None
   internetConnectivity: Optional[bool] = None
