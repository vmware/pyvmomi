# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.DirectoryServerConfig import DirectoryServerConfig

from pyVmomi.vim.vsan.FileServiceIpConfig import FileServiceIpConfig

class FileServiceDomainConfig(DynamicData):
   name: Optional[str] = None
   dnsServerAddresses: list[str] = []
   dnsSuffixes: list[str] = []
   fileServerIpConfig: list[FileServiceIpConfig] = []
   directoryServerConfig: Optional[DirectoryServerConfig] = None
   version: Optional[str] = None
