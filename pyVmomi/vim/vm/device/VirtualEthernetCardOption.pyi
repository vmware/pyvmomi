# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.option import BoolOption
from pyVmomi.vim.option import ChoiceOption

from pyVmomi.vim.vm.device import VirtualDeviceOption

class VirtualEthernetCardOption(VirtualDeviceOption):
   class NetworkBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class OpaqueNetworkBackingOption(VirtualDeviceOption.BackingOption):
      pass

   class LegacyNetworkBackingOption(VirtualDeviceOption.DeviceBackingOption):
      class LegacyNetworkDeviceName(Enum):
         bridged: ClassVar['LegacyNetworkDeviceName'] = 'bridged'
         nat: ClassVar['LegacyNetworkDeviceName'] = 'nat'
         hostonly: ClassVar['LegacyNetworkDeviceName'] = 'hostonly'

   class DistributedVirtualPortBackingOption(VirtualDeviceOption.BackingOption):
      pass

   class MacTypes(Enum):
      manual: ClassVar['MacTypes'] = 'manual'
      generated: ClassVar['MacTypes'] = 'generated'
      assigned: ClassVar['MacTypes'] = 'assigned'

   supportedOUI: ChoiceOption
   macType: ChoiceOption
   wakeOnLanEnabled: BoolOption
   vmDirectPathGen2Supported: Optional[bool] = None
   uptCompatibilityEnabled: Optional[BoolOption] = None
