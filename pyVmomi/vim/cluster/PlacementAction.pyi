# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem
from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.cluster import Action

from pyVmomi.vim.vm import RelocateSpec

class PlacementAction(Action):
   vm: Optional[VirtualMachine] = None
   targetHost: Optional[HostSystem] = None
   relocateSpec: Optional[RelocateSpec] = None
