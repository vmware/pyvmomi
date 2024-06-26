# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VmComponentProtectionSettings
from pyVmomi.vim.cluster import VmToolsMonitoringSettings

class DasVmSettings(DynamicData):
   class RestartPriority(Enum):
      disabled: ClassVar['RestartPriority'] = 'disabled'
      lowest: ClassVar['RestartPriority'] = 'lowest'
      low: ClassVar['RestartPriority'] = 'low'
      medium: ClassVar['RestartPriority'] = 'medium'
      high: ClassVar['RestartPriority'] = 'high'
      highest: ClassVar['RestartPriority'] = 'highest'
      clusterRestartPriority: ClassVar['RestartPriority'] = 'clusterRestartPriority'

   class IsolationResponse(Enum):
      none: ClassVar['IsolationResponse'] = 'none'
      powerOff: ClassVar['IsolationResponse'] = 'powerOff'
      shutdown: ClassVar['IsolationResponse'] = 'shutdown'
      clusterIsolationResponse: ClassVar['IsolationResponse'] = 'clusterIsolationResponse'

   restartPriority: Optional[str] = None
   restartPriorityTimeout: Optional[int] = None
   isolationResponse: Optional[str] = None
   vmToolsMonitoringSettings: Optional[VmToolsMonitoringSettings] = None
   vmComponentProtectionSettings: Optional[VmComponentProtectionSettings] = None
