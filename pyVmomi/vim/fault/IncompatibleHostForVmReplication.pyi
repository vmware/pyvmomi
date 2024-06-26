# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.fault import ReplicationFault

class IncompatibleHostForVmReplication(ReplicationFault):
   class IncompatibleReason(Enum):
      rpo: ClassVar['IncompatibleReason'] = 'rpo'
      netCompression: ClassVar['IncompatibleReason'] = 'netCompression'

   vmName: str
   hostName: str
   reason: str
