# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

class PerformClusterPowerActionSpec(DynamicData):
   targetPowerStatus: str
   isOrchestration: Optional[bool] = None
   initialPowerStatus: Optional[str] = None
   powerOffReason: Optional[str] = None
   infraVMs: list[VirtualMachine] = []
   infraVMUuids: list[str] = []
