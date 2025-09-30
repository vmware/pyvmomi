# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.TpmDigestInfo import TpmDigestInfo

from pyVmomi.vim.host.TpmEventLogEntry import TpmEventLogEntry

class TpmAttestationReport(DynamicData):
   tpmPcrValues: list[TpmDigestInfo] = []
   tpmEvents: list[TpmEventLogEntry] = []
   tpmLogReliable: bool
