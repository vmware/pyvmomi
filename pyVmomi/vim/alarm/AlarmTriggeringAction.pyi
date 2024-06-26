# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.action import Action

from pyVmomi.vim.alarm import AlarmAction

class AlarmTriggeringAction(AlarmAction):
   class TransitionSpec(DynamicData):
      startState: ManagedEntity.Status
      finalState: ManagedEntity.Status
      repeats: bool

   action: Action
   transitionSpecs: list[TransitionSpec] = []
   green2yellow: bool
   yellow2red: bool
   red2yellow: bool
   yellow2green: bool
