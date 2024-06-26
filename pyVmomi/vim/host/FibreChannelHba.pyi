# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.host import HostBusAdapter

class FibreChannelHba(HostBusAdapter):
   class PortType(Enum):
      fabric: ClassVar['PortType'] = 'fabric'
      loop: ClassVar['PortType'] = 'loop'
      pointToPoint: ClassVar['PortType'] = 'pointToPoint'
      unknown: ClassVar['PortType'] = 'unknown'

   portWorldWideName: long
   nodeWorldWideName: long
   portType: PortType
   speed: long
