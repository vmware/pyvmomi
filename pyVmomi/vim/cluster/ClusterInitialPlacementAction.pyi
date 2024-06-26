# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem
from pyVmomi.vim import ResourcePool

from pyVmomi.vim.cluster import Action

from pyVmomi.vim.vm import ConfigSpec

class ClusterInitialPlacementAction(Action):
   targetHost: Optional[HostSystem] = None
   pool: ResourcePool
   configSpec: Optional[ConfigSpec] = None
