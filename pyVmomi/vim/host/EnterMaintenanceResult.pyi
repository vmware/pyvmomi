# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.FaultsByHost import FaultsByHost

from pyVmomi.vim.FaultsByVM import FaultsByVM

from pyVmomi.vmodl.DynamicData import DynamicData

class EnterMaintenanceResult(DynamicData):
   vmFaults: list[FaultsByVM] = []
   hostFaults: list[FaultsByHost] = []
