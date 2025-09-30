# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.pbm.ExtendedElementDescription import ExtendedElementDescription

from pyVmomi.vmodl.DynamicData import DynamicData

class ResourceUtilization(DynamicData):
   name: ExtendedElementDescription
   description: ExtendedElementDescription
   availableBefore: Optional[long] = None
   availableAfter: Optional[long] = None
   total: Optional[long] = None
