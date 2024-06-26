# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.host import NvmeSpec

class NvmeConnectSpec(NvmeSpec):
   subnqn: str
   controllerId: Optional[int] = None
   adminQueueSize: Optional[int] = None
   keepAliveTimeout: Optional[int] = None
