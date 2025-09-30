# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.ResourcePool import ResourcePool

from pyVmomi.vim.cluster.Action import Action

from pyVmomi.vim.vm.ConfigSpec import ConfigSpec

class ClusterInitialPlacementAction(Action):
   targetHost: Optional[HostSystem] = None
   pool: ResourcePool
   configSpec: Optional[ConfigSpec] = None
