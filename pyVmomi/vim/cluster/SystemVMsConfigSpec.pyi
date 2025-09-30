# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.DatastoreUpdateSpec import DatastoreUpdateSpec

from pyVmomi.vim.cluster.TagCategoryUpdateSpec import TagCategoryUpdateSpec

class SystemVMsConfigSpec(DynamicData):
   allowedDatastores: list[DatastoreUpdateSpec] = []
   notAllowedDatastores: list[DatastoreUpdateSpec] = []
   dsTagCategoriesToExclude: list[TagCategoryUpdateSpec] = []
   deploymentMode: Optional[str] = None
