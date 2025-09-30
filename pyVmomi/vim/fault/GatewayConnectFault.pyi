# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.LocalizableMessage import LocalizableMessage

from pyVmomi.vim.fault.HostConnectFault import HostConnectFault

class GatewayConnectFault(HostConnectFault):
   gatewayType: str
   gatewayId: str
   gatewayInfo: str
   details: Optional[LocalizableMessage] = None
