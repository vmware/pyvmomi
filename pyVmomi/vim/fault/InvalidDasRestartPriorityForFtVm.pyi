# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl.fault import InvalidArgument

class InvalidDasRestartPriorityForFtVm(InvalidArgument):
   vm: VirtualMachine
   vmName: str
