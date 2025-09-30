# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.fault.ReplicationFault import ReplicationFault

class ReplicationInvalidOptions(ReplicationFault):
   options: str
   entity: Optional[ManagedEntity] = None
