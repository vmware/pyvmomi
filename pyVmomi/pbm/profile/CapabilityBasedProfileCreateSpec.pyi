# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.pbm.profile.CapabilityConstraints import CapabilityConstraints

from pyVmomi.pbm.profile.ResourceType import ResourceType

class CapabilityBasedProfileCreateSpec(DynamicData):
   name: str
   description: Optional[str] = None
   category: Optional[str] = None
   resourceType: ResourceType
   constraints: CapabilityConstraints
