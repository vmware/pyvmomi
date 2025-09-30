# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.option.BoolOption import BoolOption

from pyVmomi.vim.option.ChoiceOption import ChoiceOption

from pyVmomi.vim.option.LongOption import LongOption

from pyVmomi.vim.vm.device.VirtualDeviceOption import VirtualDeviceOption

class VirtualVMCIDeviceOption(VirtualDeviceOption):
   class FilterSpecOption(DynamicData):
      action: ChoiceOption
      protocol: ChoiceOption
      direction: ChoiceOption
      lowerDstPortBoundary: LongOption
      upperDstPortBoundary: LongOption

   allowUnrestrictedCommunication: BoolOption
   filterSpecOption: Optional[FilterSpecOption] = None
   filterSupported: Optional[BoolOption] = None
