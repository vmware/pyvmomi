# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class NetBIOSConfigInfo(DynamicData):
   class Mode(Enum):
      unknown: ClassVar['Mode'] = 'unknown'
      enabled: ClassVar['Mode'] = 'enabled'
      disabled: ClassVar['Mode'] = 'disabled'
      enabledViaDHCP: ClassVar['Mode'] = 'enabledViaDHCP'

   mode: str
