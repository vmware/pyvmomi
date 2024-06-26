# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.pbm import ExtendedElementDescription

from pyVmomi.vmodl import DynamicData

from pyVmomi.pbm.capability import PropertyMetadata

class CapabilityMetadata(DynamicData):
   class UniqueId(DynamicData):
      namespace: str
      id: str

   id: UniqueId
   summary: ExtendedElementDescription
   mandatory: Optional[bool] = None
   hint: Optional[bool] = None
   keyId: Optional[str] = None
   allowMultipleConstraints: Optional[bool] = None
   propertyMetadata: list[PropertyMetadata] = []
