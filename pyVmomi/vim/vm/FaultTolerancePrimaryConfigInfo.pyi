# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.vm import FaultToleranceConfigInfo

class FaultTolerancePrimaryConfigInfo(FaultToleranceConfigInfo):
   secondaries: list[VirtualMachine] = []
