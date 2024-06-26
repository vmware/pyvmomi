# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class NetCapabilities(DynamicData):
   canSetPhysicalNicLinkSpeed: bool
   supportsNicTeaming: bool
   nicTeamingPolicy: list[str] = []
   supportsVlan: bool
   usesServiceConsoleNic: bool
   supportsNetworkHints: bool
   maxPortGroupsPerVswitch: Optional[int] = None
   vswitchConfigSupported: bool
   vnicConfigSupported: bool
   ipRouteConfigSupported: bool
   dnsConfigSupported: bool
   dhcpOnVnicSupported: bool
   ipV6Supported: bool
   backupNfcNiocSupported: Optional[bool] = None
