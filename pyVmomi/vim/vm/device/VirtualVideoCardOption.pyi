# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.option import BoolOption
from pyVmomi.vim.option import IntOption
from pyVmomi.vim.option import LongOption

from pyVmomi.vim.vm.device import VirtualDeviceOption

class VirtualVideoCardOption(VirtualDeviceOption):
   videoRamSizeInKB: Optional[LongOption] = None
   numDisplays: Optional[IntOption] = None
   useAutoDetect: Optional[BoolOption] = None
   support3D: Optional[BoolOption] = None
   use3dRendererSupported: Optional[BoolOption] = None
   graphicsMemorySizeInKB: Optional[LongOption] = None
   graphicsMemorySizeSupported: Optional[BoolOption] = None
