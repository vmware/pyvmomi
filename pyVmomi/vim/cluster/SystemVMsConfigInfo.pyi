# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vmodl.DynamicData import DynamicData

class SystemVMsConfigInfo(DynamicData):
   class DeploymentMode(Enum):
      SYSTEM_MANAGED: ClassVar['DeploymentMode'] = 'SYSTEM_MANAGED'
      ABSENT: ClassVar['DeploymentMode'] = 'ABSENT'

   allowedDatastores: list[Datastore] = []
   notAllowedDatastores: list[Datastore] = []
   dsTagCategoriesToExclude: list[str] = []
   deploymentMode: Optional[str] = None
