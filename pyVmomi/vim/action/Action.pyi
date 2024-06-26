# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class Action(DynamicData):
   class ActionParameter(Enum):
      targetName: ClassVar['ActionParameter'] = 'targetName'
      alarmName: ClassVar['ActionParameter'] = 'alarmName'
      oldStatus: ClassVar['ActionParameter'] = 'oldStatus'
      newStatus: ClassVar['ActionParameter'] = 'newStatus'
      triggeringSummary: ClassVar['ActionParameter'] = 'triggeringSummary'
      declaringSummary: ClassVar['ActionParameter'] = 'declaringSummary'
      eventDescription: ClassVar['ActionParameter'] = 'eventDescription'
      target: ClassVar['ActionParameter'] = 'target'
      alarm: ClassVar['ActionParameter'] = 'alarm'
