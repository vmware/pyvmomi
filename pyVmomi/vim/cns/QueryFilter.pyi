# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Datastore
from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cns import Cursor
from pyVmomi.vim.cns import VolumeId

class QueryFilter(DynamicData):
   volumeIds: list[VolumeId] = []
   names: list[str] = []
   containerClusterIds: list[str] = []
   storagePolicyId: Optional[str] = None
   datastores: list[Datastore] = []
   labels: list[KeyValue] = []
   complianceStatus: Optional[str] = None
   datastoreAccessibilityStatus: Optional[str] = None
   cursor: Optional[Cursor] = None
   healthStatus: Optional[str] = None
