# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class IpConfig(DynamicData):
   class IpV6AddressConfigType(Enum):
      other: ClassVar['IpV6AddressConfigType'] = 'other'
      manual: ClassVar['IpV6AddressConfigType'] = 'manual'
      dhcp: ClassVar['IpV6AddressConfigType'] = 'dhcp'
      linklayer: ClassVar['IpV6AddressConfigType'] = 'linklayer'
      random: ClassVar['IpV6AddressConfigType'] = 'random'

   class IpV6AddressStatus(Enum):
      preferred: ClassVar['IpV6AddressStatus'] = 'preferred'
      deprecated: ClassVar['IpV6AddressStatus'] = 'deprecated'
      invalid: ClassVar['IpV6AddressStatus'] = 'invalid'
      inaccessible: ClassVar['IpV6AddressStatus'] = 'inaccessible'
      unknown: ClassVar['IpV6AddressStatus'] = 'unknown'
      tentative: ClassVar['IpV6AddressStatus'] = 'tentative'
      duplicate: ClassVar['IpV6AddressStatus'] = 'duplicate'

   class IpV6Address(DynamicData):
      ipAddress: str
      prefixLength: int
      origin: Optional[str] = None
      dadState: Optional[str] = None
      lifetime: Optional[datetime] = None
      operation: Optional[str] = None

   class IpV6AddressConfiguration(DynamicData):
      ipV6Address: list[IpV6Address] = []
      autoConfigurationEnabled: Optional[bool] = None
      dhcpV6Enabled: Optional[bool] = None

   dhcp: bool
   ipAddress: Optional[str] = None
   subnetMask: Optional[str] = None
   ipV6Config: Optional[IpV6AddressConfiguration] = None
