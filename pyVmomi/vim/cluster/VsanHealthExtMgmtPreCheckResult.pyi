# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanClusterHealthTest

class VsanHealthExtMgmtPreCheckResult(DynamicData):
   overallResult: bool
   esxVersionCheckPassed: Optional[bool] = None
   drsCheckPassed: Optional[bool] = None
   eamConnectionCheckPassed: Optional[bool] = None
   installStateCheckPassed: Optional[bool] = None
   results: list[VsanClusterHealthTest] = []
   vumRegistered: Optional[bool] = None
