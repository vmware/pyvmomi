# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class VStorageObjectQuerySpec(DynamicData):
   class QueryOperatorEnum(Enum):
      equals: ClassVar['QueryOperatorEnum'] = 'equals'
      notEquals: ClassVar['QueryOperatorEnum'] = 'notEquals'
      lessThan: ClassVar['QueryOperatorEnum'] = 'lessThan'
      greaterThan: ClassVar['QueryOperatorEnum'] = 'greaterThan'
      lessThanOrEqual: ClassVar['QueryOperatorEnum'] = 'lessThanOrEqual'
      greaterThanOrEqual: ClassVar['QueryOperatorEnum'] = 'greaterThanOrEqual'
      contains: ClassVar['QueryOperatorEnum'] = 'contains'
      startsWith: ClassVar['QueryOperatorEnum'] = 'startsWith'
      endsWith: ClassVar['QueryOperatorEnum'] = 'endsWith'

   class QueryFieldEnum(Enum):
      id: ClassVar['QueryFieldEnum'] = 'id'
      name: ClassVar['QueryFieldEnum'] = 'name'
      capacity: ClassVar['QueryFieldEnum'] = 'capacity'
      createTime: ClassVar['QueryFieldEnum'] = 'createTime'
      backingObjectId: ClassVar['QueryFieldEnum'] = 'backingObjectId'
      datastoreMoId: ClassVar['QueryFieldEnum'] = 'datastoreMoId'
      metadataKey: ClassVar['QueryFieldEnum'] = 'metadataKey'
      metadataValue: ClassVar['QueryFieldEnum'] = 'metadataValue'

   queryField: str
   queryOperator: str
   queryValue: list[str] = []
