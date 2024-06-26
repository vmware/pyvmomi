# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.vm import TargetInfo

class ScsiPassthroughInfo(TargetInfo):
   class ScsiClass(Enum):
      disk: ClassVar['ScsiClass'] = 'disk'
      tape: ClassVar['ScsiClass'] = 'tape'
      printer: ClassVar['ScsiClass'] = 'printer'
      processor: ClassVar['ScsiClass'] = 'processor'
      worm: ClassVar['ScsiClass'] = 'worm'
      cdrom: ClassVar['ScsiClass'] = 'cdrom'
      scanner: ClassVar['ScsiClass'] = 'scanner'
      optical: ClassVar['ScsiClass'] = 'optical'
      media: ClassVar['ScsiClass'] = 'media'
      com: ClassVar['ScsiClass'] = 'com'
      raid: ClassVar['ScsiClass'] = 'raid'
      unknown: ClassVar['ScsiClass'] = 'unknown'

   scsiClass: str
   vendor: str
   physicalUnitNumber: int
