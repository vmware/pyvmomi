# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanVcKmipServersHealth

from pyVmomi.vim.host import VsanEncryptionHealthSummary

class VsanClusterEncryptionHealthSummary(DynamicData):
   overallHealth: Optional[str] = None
   configHealth: Optional[str] = None
   kmsHealth: Optional[str] = None
   vcKmsResult: Optional[VsanVcKmipServersHealth] = None
   hostResults: list[VsanEncryptionHealthSummary] = []
   aesniHealth: Optional[str] = None
