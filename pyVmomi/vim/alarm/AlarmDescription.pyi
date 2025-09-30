# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.ElementDescription import ElementDescription

from pyVmomi.vim.TypeDescription import TypeDescription

from pyVmomi.vmodl.DynamicData import DynamicData

class AlarmDescription(DynamicData):
   expr: list[TypeDescription] = []
   stateOperator: list[ElementDescription] = []
   metricOperator: list[ElementDescription] = []
   hostSystemConnectionState: list[ElementDescription] = []
   virtualMachinePowerState: list[ElementDescription] = []
   datastoreConnectionState: list[ElementDescription] = []
   hostSystemPowerState: list[ElementDescription] = []
   virtualMachineGuestHeartbeatStatus: list[ElementDescription] = []
   entityStatus: list[ElementDescription] = []
   action: list[TypeDescription] = []
