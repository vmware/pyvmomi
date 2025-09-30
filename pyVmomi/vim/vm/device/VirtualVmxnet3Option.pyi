# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.option.BoolOption import BoolOption

from pyVmomi.vim.option.ChoiceOption import ChoiceOption

from pyVmomi.vim.option.IntOption import IntOption

from pyVmomi.vim.vm.device.VirtualVmxnetOption import VirtualVmxnetOption

class VirtualVmxnet3Option(VirtualVmxnetOption):
   class StrictLatencyConfigOption(DynamicData):
      allowed: BoolOption
      measureLatency: BoolOption
      maxTxQueues: IntOption
      maxRxQueues: IntOption
      txDataRingDescSize: IntOption
      rxDataRingDescSize: IntOption
      disableOffload: ChoiceOption

   uptv2Enabled: Optional[BoolOption] = None
   strictLatencyConfigOption: Optional[StrictLatencyConfigOption] = None
