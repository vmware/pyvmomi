# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class QualifiedName(DynamicData):
   class Type(Enum):
      nvmeQualifiedName: ClassVar['Type'] = 'nvmeQualifiedName'
      vvolNvmeQualifiedName: ClassVar['Type'] = 'vvolNvmeQualifiedName'

   value: str
   type: str
