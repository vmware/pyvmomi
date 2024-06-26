# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.fault import InsufficientResourcesFault

class InsufficientNetworkResourcePoolCapacity(InsufficientResourcesFault):
   dvsName: str
   dvsUuid: str
   resourcePoolKey: str
   available: long
   requested: long
   device: list[str] = []
