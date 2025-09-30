# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.vm.TargetInfo import TargetInfo

class SgxTargetInfo(TargetInfo):
   maxEpcSize: long
   flcModes: list[str] = []
   lePubKeyHashes: list[str] = []
   requireAttestationSupported: Optional[bool] = None
