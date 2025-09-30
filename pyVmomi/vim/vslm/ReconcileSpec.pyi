# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vmodl.DynamicData import DynamicData

class ReconcileSpec(DynamicData):
   datastore: Datastore
   includeDiskPaths: list[str] = []
   excludeDiskPaths: list[str] = []
   deepScan: Optional[bool] = None
   dryRun: Optional[bool] = None
   generateReport: Optional[int] = None
