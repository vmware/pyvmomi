# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.option.BoolOption import BoolOption

from pyVmomi.vim.option.IntOption import IntOption

from pyVmomi.vim.vm.device.VirtualControllerOption import VirtualControllerOption

from pyVmomi.vim.vm.device.VirtualSCSIController import VirtualSCSIController

class VirtualSCSIControllerOption(VirtualControllerOption):
   numSCSIDisks: IntOption
   numSCSICdroms: IntOption
   numSCSIPassthrough: IntOption
   sharing: list[VirtualSCSIController.Sharing] = []
   defaultSharedIndex: int
   hotAddRemove: BoolOption
   scsiCtlrUnitNumber: int
