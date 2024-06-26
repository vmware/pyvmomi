# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.host import VsanDiskEncryptionHealth
from pyVmomi.vim.host import VsanKmsHealth

from pyVmomi.vim.vsan.host import EncryptionInfo

class VsanEncryptionHealthSummary(DynamicData):
   hostname: Optional[str] = None
   encryptionInfo: Optional[EncryptionInfo] = None
   overallKmsHealth: str
   kmsHealth: list[VsanKmsHealth] = []
   encryptionIssues: list[str] = []
   diskResults: list[VsanDiskEncryptionHealth] = []
   error: Optional[MethodFault] = None
   aesniEnabled: Optional[bool] = None
   inconsistentlyEncryptedObjectCount: Optional[long] = None
   hostEncryptionDekId: Optional[str] = None
   kekVerifierHealth: Optional[bool] = None
   dekVerifierHealth: Optional[bool] = None
