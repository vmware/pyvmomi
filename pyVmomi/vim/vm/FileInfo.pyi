# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class FileInfo(DynamicData):
   vmPathName: Optional[str] = None
   snapshotDirectory: Optional[str] = None
   suspendDirectory: Optional[str] = None
   logDirectory: Optional[str] = None
   ftMetadataDirectory: Optional[str] = None
