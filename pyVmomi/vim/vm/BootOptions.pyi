# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class BootOptions(DynamicData):
   class NetworkBootProtocolType(Enum):
      ipv4: ClassVar['NetworkBootProtocolType'] = 'ipv4'
      ipv6: ClassVar['NetworkBootProtocolType'] = 'ipv6'

   class BootableDevice(DynamicData):
      pass

   class BootableDiskDevice(BootableDevice):
      deviceKey: int

   class BootableEthernetDevice(BootableDevice):
      deviceKey: int

   class BootableFloppyDevice(BootableDevice):
      pass

   class BootableCdromDevice(BootableDevice):
      pass

   bootDelay: Optional[long] = None
   enterBIOSSetup: Optional[bool] = None
   efiSecureBootEnabled: Optional[bool] = None
   bootRetryEnabled: Optional[bool] = None
   bootRetryDelay: Optional[long] = None
   bootOrder: list[BootableDevice] = []
   networkBootProtocol: Optional[str] = None
