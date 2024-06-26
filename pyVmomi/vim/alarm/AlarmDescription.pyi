# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import ElementDescription
from pyVmomi.vim import TypeDescription

from pyVmomi.vmodl import DynamicData

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
