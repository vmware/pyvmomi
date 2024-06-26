# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import DataEfficiencyConfig

from pyVmomi.vim.vsan.host import AddStoragePoolDiskSpec
from pyVmomi.vim.vsan.host import CreateNativeKeyProviderSpec
from pyVmomi.vim.vsan.host import DiskMappingCreationSpec
from pyVmomi.vim.vsan.host import EncryptionInfo

class VsanPrepareVsanForVcsaSpec(DynamicData):
   vsanDiskMappingCreationSpec: Optional[DiskMappingCreationSpec] = None
   vsanDataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   taskId: Optional[str] = None
   vsanDataEncryptionConfig: Optional[EncryptionInfo] = None
   vsanAddStoragePoolDiskSpec: Optional[AddStoragePoolDiskSpec] = None
   createNativeKeyProviderSpec: Optional[CreateNativeKeyProviderSpec] = None
