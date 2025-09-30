# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.fault.InsufficientResourcesFault import InsufficientResourcesFault

class InsufficientVFlashResourcesFault(InsufficientResourcesFault):
   freeSpaceInMB: Optional[long] = None
   freeSpace: long
   requestedSpaceInMB: Optional[long] = None
   requestedSpace: long
