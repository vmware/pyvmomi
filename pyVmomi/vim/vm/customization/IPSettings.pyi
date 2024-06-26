# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm.customization import IpGenerator
from pyVmomi.vim.vm.customization import IpV6Generator

class IPSettings(DynamicData):
   class IpV6AddressSpec(DynamicData):
      ip: list[IpV6Generator] = []
      gateway: list[str] = []

   class NetBIOSMode(Enum):
      enableNetBIOSViaDhcp: ClassVar['NetBIOSMode'] = 'enableNetBIOSViaDhcp'
      enableNetBIOS: ClassVar['NetBIOSMode'] = 'enableNetBIOS'
      disableNetBIOS: ClassVar['NetBIOSMode'] = 'disableNetBIOS'

   ip: IpGenerator
   subnetMask: Optional[str] = None
   gateway: list[str] = []
   ipV6Spec: Optional[IpV6AddressSpec] = None
   dnsServerList: list[str] = []
   dnsDomain: Optional[str] = None
   primaryWINS: Optional[str] = None
   secondaryWINS: Optional[str] = None
   netBIOS: Optional[NetBIOSMode] = None
