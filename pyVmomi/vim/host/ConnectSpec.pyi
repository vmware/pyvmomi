# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Folder

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import GatewaySpec
from pyVmomi.vim.host import HostAccessManager

class ConnectSpec(DynamicData):
   hostName: Optional[str] = None
   port: Optional[int] = None
   sslThumbprint: Optional[str] = None
   userName: Optional[str] = None
   password: Optional[str] = None
   vmFolder: Optional[Folder] = None
   force: bool
   vimAccountName: Optional[str] = None
   vimAccountPassword: Optional[str] = None
   managementIp: Optional[str] = None
   lockdownMode: Optional[HostAccessManager.LockdownMode] = None
   hostGateway: Optional[GatewaySpec] = None
