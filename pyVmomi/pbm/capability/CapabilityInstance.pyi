# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.pbm.capability.CapabilityMetadata import CapabilityMetadata

from pyVmomi.pbm.capability.ConstraintInstance import ConstraintInstance

class CapabilityInstance(DynamicData):
   id: CapabilityMetadata.UniqueId
   constraint: list[ConstraintInstance] = []
