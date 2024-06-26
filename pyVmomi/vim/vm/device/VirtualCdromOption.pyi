# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.option import BoolOption

from pyVmomi.vim.vm.device import VirtualDeviceOption

class VirtualCdromOption(VirtualDeviceOption):
   class IsoBackingOption(VirtualDeviceOption.FileBackingOption):
      pass

   class PassthroughBackingOption(VirtualDeviceOption.DeviceBackingOption):
      exclusive: BoolOption

   class RemotePassthroughBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
      exclusive: BoolOption

   class AtapiBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class RemoteAtapiBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass
