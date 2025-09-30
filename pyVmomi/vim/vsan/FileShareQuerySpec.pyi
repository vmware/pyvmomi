# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.FileShareQueryProperties import FileShareQueryProperties

class FileShareQuerySpec(DynamicData):
   domainName: Optional[str] = None
   uuids: list[str] = []
   names: list[str] = []
   offset: Optional[str] = None
   limit: Optional[long] = None
   managedBy: list[str] = []
   protocols: list[str] = []
   pageNumber: Optional[long] = None
   properties: Optional[FileShareQueryProperties] = None
