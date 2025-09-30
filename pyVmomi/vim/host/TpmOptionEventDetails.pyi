# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import byte

from pyVmomi.vim.host.TpmEventDetails import TpmEventDetails

class TpmOptionEventDetails(TpmEventDetails):
   optionsFileName: str
   bootOptions: list[byte] = []
