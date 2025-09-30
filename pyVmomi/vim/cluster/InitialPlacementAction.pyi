# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.ResourcePool import ResourcePool

from pyVmomi.vim.cluster.Action import Action

class InitialPlacementAction(Action):
   targetHost: HostSystem
   pool: Optional[ResourcePool] = None
