# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import binary

from pyVmomi.vim.host import NvmeTransportParameters

class NvmeOpaqueTransportParameters(NvmeTransportParameters):
   trtype: str
   traddr: str
   adrfam: str
   trsvcid: str
   tsas: binary
