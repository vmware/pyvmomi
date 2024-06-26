# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vsan import DirectoryServerConfig

class ActiveDirectoryServerConfig(DirectoryServerConfig):
   activeDirectoryDomainName: Optional[str] = None
   username: Optional[str] = None
   password: Optional[str] = None
   organizationalUnit: Optional[str] = None
   preferredADServers: list[str] = []
