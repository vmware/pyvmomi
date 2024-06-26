# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.pbm import ServerObjectRef

from pyVmomi.vmodl import DynamicData

class FetchEntityHealthStatusSpec(DynamicData):
   objectRef: ServerObjectRef
   backingId: Optional[str] = None
