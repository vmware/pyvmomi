# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData

class DasAamNodeState(DynamicData):
   class DasState(Enum):
      uninitialized: ClassVar['DasState'] = 'uninitialized'
      initialized: ClassVar['DasState'] = 'initialized'
      configuring: ClassVar['DasState'] = 'configuring'
      unconfiguring: ClassVar['DasState'] = 'unconfiguring'
      running: ClassVar['DasState'] = 'running'
      error: ClassVar['DasState'] = 'error'
      agentShutdown: ClassVar['DasState'] = 'agentShutdown'
      nodeFailed: ClassVar['DasState'] = 'nodeFailed'

   host: HostSystem
   name: str
   configState: str
   runtimeState: str
