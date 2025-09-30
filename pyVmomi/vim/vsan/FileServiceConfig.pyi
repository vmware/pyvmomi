# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.Network import Network

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.FileServiceDomainConfig import FileServiceDomainConfig

class FileServiceConfig(DynamicData):
   enabled: bool
   fileServerMemoryMB: Optional[long] = None
   fileServerCPUMhz: Optional[long] = None
   fsvmMemoryMB: Optional[long] = None
   fsvmCPU: Optional[long] = None
   network: Optional[Network] = None
   domains: list[FileServiceDomainConfig] = []
   fileAnalyticsEnabled: Optional[bool] = None
