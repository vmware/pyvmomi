# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanVcKmipServersHealth import VsanVcKmipServersHealth

from pyVmomi.vim.host.VsanEncryptionHealthSummary import VsanEncryptionHealthSummary

class VsanClusterEncryptionHealthSummary(DynamicData):
   overallHealth: Optional[str] = None
   configHealth: Optional[str] = None
   kmsHealth: Optional[str] = None
   vcKmsResult: Optional[VsanVcKmipServersHealth] = None
   hostResults: list[VsanEncryptionHealthSummary] = []
   aesniHealth: Optional[str] = None
