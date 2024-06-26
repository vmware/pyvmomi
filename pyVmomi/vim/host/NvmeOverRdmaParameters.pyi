# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.host import NvmeTransportParameters

class NvmeOverRdmaParameters(NvmeTransportParameters):
   address: str
   addressFamily: Optional[str] = None
   portNumber: Optional[int] = None
