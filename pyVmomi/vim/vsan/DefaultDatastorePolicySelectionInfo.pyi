# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

class DefaultDatastorePolicySelectionInfo(DynamicData):
   enabled: bool
   defaultPolicyId: Optional[str] = None
   lastPolicySelectionTime: Optional[datetime] = None
