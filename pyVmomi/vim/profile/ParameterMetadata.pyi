# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ExtendedElementDescription

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.profile import ProfilePropertyPath

class ParameterMetadata(DynamicData):
   class RelationType(Enum):
      dynamic_relation: ClassVar['RelationType'] = 'dynamic_relation'
      extensible_relation: ClassVar['RelationType'] = 'extensible_relation'
      localizable_relation: ClassVar['RelationType'] = 'localizable_relation'
      static_relation: ClassVar['RelationType'] = 'static_relation'
      validation_relation: ClassVar['RelationType'] = 'validation_relation'

   class ParameterRelationMetadata(DynamicData):
      relationTypes: list[str] = []
      values: list[object] = []
      path: Optional[ProfilePropertyPath] = None
      minCount: int
      maxCount: int

   id: ExtendedElementDescription
   type: type
   optional: bool
   defaultValue: Optional[object] = None
   hidden: Optional[bool] = None
   securitySensitive: Optional[bool] = None
   readOnly: Optional[bool] = None
   parameterRelations: list[ParameterRelationMetadata] = []
