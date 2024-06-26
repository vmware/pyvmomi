# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.profile import ApplyProfile

from pyVmomi.vim.profile.host import IpRouteProfile
from pyVmomi.vim.profile.host import NetworkProfile

class NetStackInstanceProfile(ApplyProfile):
   key: str
   dnsConfig: NetworkProfile.DnsConfigProfile
   ipRouteConfig: IpRouteProfile
