# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.host import DnsConfig
from pyVmomi.vim.host import VirtualNicConnection

class DnsConfigSpec(DnsConfig):
   virtualNicConnection: Optional[VirtualNicConnection] = None
   virtualNicConnectionV6: Optional[VirtualNicConnection] = None
