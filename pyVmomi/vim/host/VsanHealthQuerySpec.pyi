# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VsanHealthQuerySpec(DynamicData):
   includeAllRemoteClusters: Optional[bool] = None
   remoteClusterUuids: list[str] = []
   latencyOnly: Optional[bool] = None
   mode: Optional[str] = None
