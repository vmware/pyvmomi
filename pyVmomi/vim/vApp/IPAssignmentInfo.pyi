# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class IPAssignmentInfo(DynamicData):
   class IpAllocationPolicy(Enum):
      dhcpPolicy: ClassVar['IpAllocationPolicy'] = 'dhcpPolicy'
      transientPolicy: ClassVar['IpAllocationPolicy'] = 'transientPolicy'
      fixedPolicy: ClassVar['IpAllocationPolicy'] = 'fixedPolicy'
      fixedAllocatedPolicy: ClassVar['IpAllocationPolicy'] = 'fixedAllocatedPolicy'

   class AllocationSchemes(Enum):
      dhcp: ClassVar['AllocationSchemes'] = 'dhcp'
      ovfenv: ClassVar['AllocationSchemes'] = 'ovfenv'

   class Protocols(Enum):
      IPv4: ClassVar['Protocols'] = 'IPv4'
      IPv6: ClassVar['Protocols'] = 'IPv6'

   supportedAllocationScheme: list[str] = []
   ipAllocationPolicy: Optional[str] = None
   supportedIpProtocol: list[str] = []
   ipProtocol: Optional[str] = None
