# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import VsanDownloadItem

class VsanHostCimProviderInfo(DynamicData):
   cimProviderSupported: Optional[bool] = None
   installedCIMProvider: Optional[str] = None
   cimProviderOnHcl: list[str] = []
   cimProviderLinksOnHcl: list[VsanDownloadItem] = []
