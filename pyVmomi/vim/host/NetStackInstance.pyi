# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import DnsConfig
from pyVmomi.vim.host import IpRouteConfig
from pyVmomi.vim.host import IpRouteTableConfig

class NetStackInstance(DynamicData):
   class SystemStackKey(Enum):
      defaultTcpipStack: ClassVar['SystemStackKey'] = 'defaultTcpipStack'
      vmotion: ClassVar['SystemStackKey'] = 'vmotion'
      vSphereProvisioning: ClassVar['SystemStackKey'] = 'vSphereProvisioning'
      mirror: ClassVar['SystemStackKey'] = 'mirror'
      ops: ClassVar['SystemStackKey'] = 'ops'

   class CongestionControlAlgorithmType(Enum):
      newreno: ClassVar['CongestionControlAlgorithmType'] = 'newreno'
      cubic: ClassVar['CongestionControlAlgorithmType'] = 'cubic'

   key: Optional[str] = None
   name: Optional[str] = None
   dnsConfig: Optional[DnsConfig] = None
   ipRouteConfig: Optional[IpRouteConfig] = None
   requestedMaxNumberOfConnections: Optional[int] = None
   congestionControlAlgorithm: Optional[str] = None
   ipV6Enabled: Optional[bool] = None
   routeTableConfig: Optional[IpRouteTableConfig] = None
