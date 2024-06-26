# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

class VVolVmConfigFileUpdateResult(DynamicData):
   class FailedVmConfigFileInfo(DynamicData):
      targetConfigVVolId: str
      dsPath: Optional[str] = None
      fault: MethodFault

   succeededVmConfigFile: list[KeyValue] = []
   failedVmConfigFile: list[FailedVmConfigFileInfo] = []
