# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.option.ChoiceOption import ChoiceOption

from pyVmomi.vim.vm.device.VirtualVmxnet3Option import VirtualVmxnet3Option

class VirtualVmxnet3VrdmaOption(VirtualVmxnet3Option):
   class DeviceProtocols(Enum):
      rocev1: ClassVar['DeviceProtocols'] = 'rocev1'
      rocev2: ClassVar['DeviceProtocols'] = 'rocev2'

   deviceProtocol: Optional[ChoiceOption] = None
