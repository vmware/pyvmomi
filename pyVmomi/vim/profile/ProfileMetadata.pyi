# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ExtendedDescription import ExtendedDescription

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.LocalizableMessage import LocalizableMessage

class ProfileMetadata(DynamicData):
   class ProfileSortSpec(DynamicData):
      policyId: str
      parameter: str

   class ProfileOperationMessage(DynamicData):
      operationName: str
      message: LocalizableMessage

   key: type
   profileTypeName: Optional[str] = None
   description: Optional[ExtendedDescription] = None
   sortSpec: list[ProfileSortSpec] = []
   profileCategory: Optional[str] = None
   profileComponent: Optional[str] = None
   operationMessages: list[ProfileOperationMessage] = []
