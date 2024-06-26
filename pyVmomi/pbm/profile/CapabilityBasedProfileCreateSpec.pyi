# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.pbm.profile import CapabilityConstraints
from pyVmomi.pbm.profile import ResourceType

class CapabilityBasedProfileCreateSpec(DynamicData):
   name: str
   description: Optional[str] = None
   category: Optional[str] = None
   resourceType: ResourceType
   constraints: CapabilityConstraints
