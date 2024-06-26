# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

class ClusterStatus(DynamicData):
   class State(DynamicData):
      class CompletionEstimate(DynamicData):
         completeTime: Optional[datetime] = None
         percentComplete: Optional[int] = None

      state: str
      completion: Optional[CompletionEstimate] = None

   uuid: Optional[str] = None
   nodeUuid: Optional[str] = None
   health: str
   nodeState: State
   memberUuid: list[str] = []
