# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import PropertyPath

from pyVmomi.vmodl.DynamicData import DynamicData

class ProfilePropertyPath(DynamicData):
   profilePath: PropertyPath
   policyId: Optional[str] = None
   parameterId: Optional[str] = None
   policyOptionId: Optional[str] = None
