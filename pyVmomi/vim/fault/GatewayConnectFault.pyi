# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import LocalizableMessage

from pyVmomi.vim.fault import HostConnectFault

class GatewayConnectFault(HostConnectFault):
   gatewayType: str
   gatewayId: str
   gatewayInfo: str
   details: Optional[LocalizableMessage] = None
