# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vim.fault.InvalidState import InvalidState

class CannotPowerOffVmInCluster(InvalidState):
   class Operation(Enum):
      suspend: ClassVar['Operation'] = 'suspend'
      powerOff: ClassVar['Operation'] = 'powerOff'
      guestShutdown: ClassVar['Operation'] = 'guestShutdown'
      guestSuspend: ClassVar['Operation'] = 'guestSuspend'

   operation: str
   vm: VirtualMachine
   vmName: str
