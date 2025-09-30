# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.ElementDescription import ElementDescription

from pyVmomi.vmodl.DynamicData import DynamicData

class SystemIdentificationInfo(DynamicData):
   class Identifier(Enum):
      AssetTag: ClassVar['Identifier'] = 'AssetTag'
      ServiceTag: ClassVar['Identifier'] = 'ServiceTag'
      OemSpecificString: ClassVar['Identifier'] = 'OemSpecificString'
      EnclosureSerialNumberTag: ClassVar['Identifier'] = 'EnclosureSerialNumberTag'
      SerialNumberTag: ClassVar['Identifier'] = 'SerialNumberTag'

   identifierValue: str
   identifierType: ElementDescription
