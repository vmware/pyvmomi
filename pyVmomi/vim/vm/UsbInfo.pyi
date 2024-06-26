# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.vm import Summary
from pyVmomi.vim.vm import TargetInfo

class UsbInfo(TargetInfo):
   class Speed(Enum):
      low: ClassVar['Speed'] = 'low'
      full: ClassVar['Speed'] = 'full'
      high: ClassVar['Speed'] = 'high'
      superSpeed: ClassVar['Speed'] = 'superSpeed'
      superSpeedPlus: ClassVar['Speed'] = 'superSpeedPlus'
      superSpeed20Gbps: ClassVar['Speed'] = 'superSpeed20Gbps'
      unknownSpeed: ClassVar['Speed'] = 'unknownSpeed'

   class Family(Enum):
      audio: ClassVar['Family'] = 'audio'
      hid: ClassVar['Family'] = 'hid'
      hid_bootable: ClassVar['Family'] = 'hid_bootable'
      physical: ClassVar['Family'] = 'physical'
      communication: ClassVar['Family'] = 'communication'
      imaging: ClassVar['Family'] = 'imaging'
      printer: ClassVar['Family'] = 'printer'
      storage: ClassVar['Family'] = 'storage'
      hub: ClassVar['Family'] = 'hub'
      smart_card: ClassVar['Family'] = 'smart_card'
      security: ClassVar['Family'] = 'security'
      video: ClassVar['Family'] = 'video'
      wireless: ClassVar['Family'] = 'wireless'
      bluetooth: ClassVar['Family'] = 'bluetooth'
      wusb: ClassVar['Family'] = 'wusb'
      pda: ClassVar['Family'] = 'pda'
      vendor_specific: ClassVar['Family'] = 'vendor_specific'
      other: ClassVar['Family'] = 'other'
      unknownFamily: ClassVar['Family'] = 'unknownFamily'

   description: str
   vendor: int
   product: int
   physicalPath: str
   family: list[str] = []
   speed: list[str] = []
   summary: Optional[Summary] = None
