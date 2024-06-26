# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import binary

from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import DynamicData

class EntityBackup(DynamicData):
   class Config(DynamicData):
      entityType: str
      configBlob: binary
      key: Optional[str] = None
      name: Optional[str] = None
      container: Optional[ManagedEntity] = None
      configVersion: Optional[str] = None

   class EntityType(Enum):
      distributedVirtualSwitch: ClassVar['EntityType'] = 'distributedVirtualSwitch'
      distributedVirtualPortgroup: ClassVar['EntityType'] = 'distributedVirtualPortgroup'

   class ImportType(Enum):
      createEntityWithNewIdentifier: ClassVar['ImportType'] = 'createEntityWithNewIdentifier'
      createEntityWithOriginalIdentifier: ClassVar['ImportType'] = 'createEntityWithOriginalIdentifier'
      applyToEntitySpecified: ClassVar['ImportType'] = 'applyToEntitySpecified'
