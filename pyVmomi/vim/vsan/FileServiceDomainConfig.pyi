# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import DirectoryServerConfig
from pyVmomi.vim.vsan import FileServiceIpConfig

class FileServiceDomainConfig(DynamicData):
   name: Optional[str] = None
   dnsServerAddresses: list[str] = []
   dnsSuffixes: list[str] = []
   fileServerIpConfig: list[FileServiceIpConfig] = []
   directoryServerConfig: Optional[DirectoryServerConfig] = None
   version: Optional[str] = None
