# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.pbm.ExtendedElementDescription import ExtendedElementDescription

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.pbm.capability.TypeInfo import TypeInfo

class PropertyMetadata(DynamicData):
   id: str
   summary: ExtendedElementDescription
   mandatory: bool
   type: Optional[TypeInfo] = None
   defaultValue: Optional[object] = None
   allowedValue: Optional[object] = None
   requirementsTypeHint: Optional[str] = None
