# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Network

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import FileServiceDomainConfig

class FileServiceConfig(DynamicData):
   enabled: bool
   fileServerMemoryMB: Optional[long] = None
   fileServerCPUMhz: Optional[long] = None
   fsvmMemoryMB: Optional[long] = None
   fsvmCPU: Optional[long] = None
   network: Optional[Network] = None
   domains: list[FileServiceDomainConfig] = []
   fileAnalyticsEnabled: Optional[bool] = None
