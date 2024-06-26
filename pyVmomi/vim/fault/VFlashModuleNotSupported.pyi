# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.fault import VmConfigFault

class VFlashModuleNotSupported(VmConfigFault):
   class Reason(Enum):
      CacheModeNotSupported: ClassVar['Reason'] = 'CacheModeNotSupported'
      CacheConsistencyTypeNotSupported: ClassVar['Reason'] = 'CacheConsistencyTypeNotSupported'
      CacheBlockSizeNotSupported: ClassVar['Reason'] = 'CacheBlockSizeNotSupported'
      CacheReservationNotSupported: ClassVar['Reason'] = 'CacheReservationNotSupported'
      DiskSizeNotSupported: ClassVar['Reason'] = 'DiskSizeNotSupported'

   vmName: str
   moduleName: str
   reason: str
   hostName: str
