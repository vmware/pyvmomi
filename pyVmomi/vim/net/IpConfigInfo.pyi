# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.net import DhcpConfigInfo

class IpConfigInfo(DynamicData):
   class IpAddressOrigin(Enum):
      other: ClassVar['IpAddressOrigin'] = 'other'
      manual: ClassVar['IpAddressOrigin'] = 'manual'
      dhcp: ClassVar['IpAddressOrigin'] = 'dhcp'
      linklayer: ClassVar['IpAddressOrigin'] = 'linklayer'
      random: ClassVar['IpAddressOrigin'] = 'random'

   class IpAddressStatus(Enum):
      preferred: ClassVar['IpAddressStatus'] = 'preferred'
      deprecated: ClassVar['IpAddressStatus'] = 'deprecated'
      invalid: ClassVar['IpAddressStatus'] = 'invalid'
      inaccessible: ClassVar['IpAddressStatus'] = 'inaccessible'
      unknown: ClassVar['IpAddressStatus'] = 'unknown'
      tentative: ClassVar['IpAddressStatus'] = 'tentative'
      duplicate: ClassVar['IpAddressStatus'] = 'duplicate'

   class IpAddress(DynamicData):
      ipAddress: str
      prefixLength: int
      origin: Optional[str] = None
      state: Optional[str] = None
      lifetime: Optional[datetime] = None

   ipAddress: list[IpAddress] = []
   dhcp: Optional[DhcpConfigInfo] = None
   autoConfigurationEnabled: Optional[bool] = None
