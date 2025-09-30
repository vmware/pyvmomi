# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl.DynamicData import DynamicData

class TdxInfo(DynamicData):
   class TdxState(Enum):
      initializing: ClassVar['TdxState'] = 'initializing'
      initialized: ClassVar['TdxState'] = 'initialized'
      configured: ClassVar['TdxState'] = 'configured'
      ready: ClassVar['TdxState'] = 'ready'
      disabledBios: ClassVar['TdxState'] = 'disabledBios'

   tdxState: str
   numTDXPrivateKeyIDs: int
