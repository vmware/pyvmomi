# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class UnresolvedVmfsResolutionSpec(DynamicData):
   class VmfsUuidResolution(Enum):
      resignature: ClassVar['VmfsUuidResolution'] = 'resignature'
      forceMount: ClassVar['VmfsUuidResolution'] = 'forceMount'

   extentDevicePath: list[str] = []
   uuidResolution: str
