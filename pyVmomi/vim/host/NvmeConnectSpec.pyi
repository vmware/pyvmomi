# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.host.NvmeSpec import NvmeSpec

class NvmeConnectSpec(NvmeSpec):
   subnqn: str
   controllerId: Optional[int] = None
   adminQueueSize: Optional[int] = None
   keepAliveTimeout: Optional[int] = None
