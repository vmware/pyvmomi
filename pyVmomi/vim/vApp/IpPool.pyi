# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Network

from pyVmomi.vmodl import DynamicData

class IpPool(DynamicData):
   class IpPoolConfigInfo(DynamicData):
      subnetAddress: Optional[str] = None
      netmask: Optional[str] = None
      gateway: Optional[str] = None
      range: Optional[str] = None
      dns: list[str] = []
      dhcpServerAvailable: Optional[bool] = None
      ipPoolEnabled: Optional[bool] = None

   class Association(DynamicData):
      network: Optional[Network] = None
      networkName: str

   id: Optional[int] = None
   name: Optional[str] = None
   ipv4Config: Optional[IpPoolConfigInfo] = None
   ipv6Config: Optional[IpPoolConfigInfo] = None
   dnsDomain: Optional[str] = None
   dnsSearchPath: Optional[str] = None
   hostPrefix: Optional[str] = None
   httpProxy: Optional[str] = None
   networkAssociation: list[Association] = []
   availableIpv4Addresses: Optional[int] = None
   availableIpv6Addresses: Optional[int] = None
   allocatedIpv4Addresses: Optional[int] = None
   allocatedIpv6Addresses: Optional[int] = None
