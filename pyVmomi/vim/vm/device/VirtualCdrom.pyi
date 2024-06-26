# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.vm.device import VirtualDevice

class VirtualCdrom(VirtualDevice):
   class IsoBackingInfo(VirtualDevice.FileBackingInfo):
      pass

   class PassthroughBackingInfo(VirtualDevice.DeviceBackingInfo):
      exclusive: bool

   class RemotePassthroughBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      exclusive: bool

   class AtapiBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class RemoteAtapiBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      pass
