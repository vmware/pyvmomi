# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import DynamicData

class HealthUpdate(DynamicData):
   entity: ManagedEntity
   healthUpdateInfoId: str
   id: str
   status: ManagedEntity.Status
   remediation: str
