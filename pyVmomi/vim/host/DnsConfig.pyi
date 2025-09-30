# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

class DnsConfig(DynamicData):
   dhcp: bool
   virtualNicDevice: Optional[str] = None
   ipv6VirtualNicDevice: Optional[str] = None
   hostName: str
   domainName: str
   address: list[str] = []
   searchDomain: list[str] = []
