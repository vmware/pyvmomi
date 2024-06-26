# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm import ProfileSpec

from pyVmomi.vim.vsan import FileShareNetPermission
from pyVmomi.vim.vsan import FileShareSmbOptions

class FileShareConfig(DynamicData):
   name: Optional[str] = None
   domainName: Optional[str] = None
   quota: Optional[str] = None
   softQuota: Optional[str] = None
   labels: list[KeyValue] = []
   storagePolicy: Optional[ProfileSpec] = None
   permission: list[FileShareNetPermission] = []
   protocols: list[str] = []
   smbOptions: Optional[FileShareSmbOptions] = None
   nfsSecType: Optional[str] = None
   affinityLocation: Optional[str] = None
