# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.vsan.ResourceCheckComponentResult import ResourceCheckComponentResult

class ResourceCheckDataPersistenceResult(ResourceCheckComponentResult):
   dataToRebuild: Optional[long] = None
   inaccessibleInstances: list[str] = []
   reducedAvailabilityInstances: list[str] = []
   rebuildInstances: list[str] = []
