# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VsanFileServerHealthSummary(DynamicData):
   domainName: Optional[str] = None
   fileServerIp: Optional[str] = None
   nfsdHealth: Optional[str] = None
   networkHealth: Optional[str] = None
   rootfsHealth: Optional[str] = None
   description: Optional[str] = None
   smbConnections: Optional[int] = None
   smbDaemonHealth: Optional[str] = None
   adTestJoinHealth: Optional[str] = None
   dnsLookupHealth: Optional[str] = None
