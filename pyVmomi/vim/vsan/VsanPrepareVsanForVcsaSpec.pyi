# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.DataEfficiencyConfig import DataEfficiencyConfig

from pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec import AddStoragePoolDiskSpec

from pyVmomi.vim.vsan.host.CreateNativeKeyProviderSpec import CreateNativeKeyProviderSpec

from pyVmomi.vim.vsan.host.DiskMappingCreationSpec import DiskMappingCreationSpec

from pyVmomi.vim.vsan.host.EncryptionInfo import EncryptionInfo

class VsanPrepareVsanForVcsaSpec(DynamicData):
   vsanDiskMappingCreationSpec: Optional[DiskMappingCreationSpec] = None
   vsanDataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   taskId: Optional[str] = None
   vsanDataEncryptionConfig: Optional[EncryptionInfo] = None
   vsanAddStoragePoolDiskSpec: Optional[AddStoragePoolDiskSpec] = None
   createNativeKeyProviderSpec: Optional[CreateNativeKeyProviderSpec] = None
