# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import DynamicData

class RuleInfo(DynamicData):
   key: Optional[int] = None
   status: Optional[ManagedEntity.Status] = None
   enabled: Optional[bool] = None
   name: Optional[str] = None
   mandatory: Optional[bool] = None
   userCreated: Optional[bool] = None
   inCompliance: Optional[bool] = None
   ruleUuid: Optional[str] = None
