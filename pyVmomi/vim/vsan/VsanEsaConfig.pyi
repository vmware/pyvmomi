# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.VsanDatastoreDefaultPolicySelectionConfig import VsanDatastoreDefaultPolicySelectionConfig

from pyVmomi.vim.vsan.VsanEsaDiskConfiguration import VsanEsaDiskConfiguration

from pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec import AddStoragePoolDiskSpec

class VsanEsaConfig(DynamicData):
   storagePoolSpecs: list[AddStoragePoolDiskSpec] = []
   hclDiskClaimEnabled: Optional[bool] = None
   datastoreDefaultPolicySelectionConfig: Optional[VsanDatastoreDefaultPolicySelectionConfig] = None
   diskConfiguration: Optional[VsanEsaDiskConfiguration] = None
