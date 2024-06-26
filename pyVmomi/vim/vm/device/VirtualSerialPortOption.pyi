# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.option import BoolOption
from pyVmomi.vim.option import ChoiceOption

from pyVmomi.vim.vm.device import VirtualDeviceOption

class VirtualSerialPortOption(VirtualDeviceOption):
   class EndPoint(Enum):
      client: ClassVar['EndPoint'] = 'client'
      server: ClassVar['EndPoint'] = 'server'

   class FileBackingOption(VirtualDeviceOption.FileBackingOption):
      pass

   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class PipeBackingOption(VirtualDeviceOption.PipeBackingOption):
      endpoint: ChoiceOption
      noRxLoss: BoolOption

   class URIBackingOption(VirtualDeviceOption.URIBackingOption):
      pass

   class ThinPrintBackingOption(VirtualDeviceOption.BackingOption):
      pass

   yieldOnPoll: BoolOption
