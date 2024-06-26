# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.option import StringOption

from pyVmomi.vim.vm.device import VirtualDeviceOption

class VirtualPCIPassthroughOption(VirtualDeviceOption):
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class PluginBackingOption(VirtualDeviceOption.BackingOption):
      pass

   class VmiopBackingOption(PluginBackingOption):
      vgpu: StringOption
      maxInstances: int

   class DynamicBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class DvxBackingOption(VirtualDeviceOption.BackingOption):
      pass
