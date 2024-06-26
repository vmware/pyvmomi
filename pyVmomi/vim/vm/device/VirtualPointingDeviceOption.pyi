# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.option import ChoiceOption

from pyVmomi.vim.vm.device import VirtualDeviceOption

class VirtualPointingDeviceOption(VirtualDeviceOption):
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      class HostPointingDeviceChoice(Enum):
         autodetect: ClassVar['HostPointingDeviceChoice'] = 'autodetect'
         intellimouseExplorer: ClassVar['HostPointingDeviceChoice'] = 'intellimouseExplorer'
         intellimousePs2: ClassVar['HostPointingDeviceChoice'] = 'intellimousePs2'
         logitechMouseman: ClassVar['HostPointingDeviceChoice'] = 'logitechMouseman'
         microsoft_serial: ClassVar['HostPointingDeviceChoice'] = 'microsoft_serial'
         mouseSystems: ClassVar['HostPointingDeviceChoice'] = 'mouseSystems'
         mousemanSerial: ClassVar['HostPointingDeviceChoice'] = 'mousemanSerial'
         ps2: ClassVar['HostPointingDeviceChoice'] = 'ps2'

      hostPointingDevice: ChoiceOption
