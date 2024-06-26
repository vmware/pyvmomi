# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import DatastoreUpdateSpec
from pyVmomi.vim.cluster import TagCategoryUpdateSpec

class SystemVMsConfigSpec(DynamicData):
   allowedDatastores: list[DatastoreUpdateSpec] = []
   notAllowedDatastores: list[DatastoreUpdateSpec] = []
   dsTagCategoriesToExclude: list[TagCategoryUpdateSpec] = []
   deploymentMode: Optional[str] = None
