# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.KeyValue import KeyValue

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vm.ProfileSpec import ProfileSpec

from pyVmomi.vim.vsan.FileShareNetPermission import FileShareNetPermission

from pyVmomi.vim.vsan.FileShareSmbOptions import FileShareSmbOptions

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
