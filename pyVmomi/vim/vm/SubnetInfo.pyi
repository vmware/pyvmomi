# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Folder import Folder

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vm.TargetInfo import TargetInfo

class SubnetInfo(TargetInfo):
   class FolderInfo(DynamicData):
      name: str
      folder: Folder

   id: str
   subnetFolderInfo: FolderInfo
   vpcFolderInfo: FolderInfo
   projectFolderInfo: Optional[FolderInfo] = None
   rootFolderInfo: FolderInfo
