# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import PropertyPath

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import BoolOption
from pyVmomi.vim.option import ChoiceOption

class VirtualDeviceOption(DynamicData):
   class BackingOption(DynamicData):
      type: type

   class FileBackingOption(BackingOption):
      class FileExtension(Enum):
         iso: ClassVar['FileExtension'] = 'iso'
         flp: ClassVar['FileExtension'] = 'flp'
         vmdk: ClassVar['FileExtension'] = 'vmdk'
         dsk: ClassVar['FileExtension'] = 'dsk'
         rdm: ClassVar['FileExtension'] = 'rdm'

      fileNameExtensions: Optional[ChoiceOption] = None

   class DeviceBackingOption(BackingOption):
      autoDetectAvailable: BoolOption

   class RemoteDeviceBackingOption(BackingOption):
      autoDetectAvailable: BoolOption

   class PipeBackingOption(BackingOption):
      pass

   class URIBackingOption(BackingOption):
      class Direction(Enum):
         server: ClassVar['Direction'] = 'server'
         client: ClassVar['Direction'] = 'client'

      directions: ChoiceOption

   class ConnectOption(DynamicData):
      startConnected: BoolOption
      allowGuestControl: BoolOption

   class BusSlotOption(DynamicData):
      type: type

   type: type
   connectOption: Optional[ConnectOption] = None
   busSlotOption: Optional[BusSlotOption] = None
   controllerType: Optional[type] = None
   autoAssignController: Optional[BoolOption] = None
   backingOption: list[BackingOption] = []
   defaultBackingOptionIndex: Optional[int] = None
   licensingLimit: list[PropertyPath] = []
   deprecated: bool
   plugAndPlay: bool
   hotRemoveSupported: bool
   numaSupported: Optional[bool] = None
