# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.net import DhcpConfigSpec

class IpConfigSpec(DynamicData):
   class IpAddressSpec(DynamicData):
      ipAddress: str
      prefixLength: int
      operation: str

   ipAddress: list[IpAddressSpec] = []
   dhcp: Optional[DhcpConfigSpec] = None
   autoConfigurationEnabled: Optional[bool] = None
