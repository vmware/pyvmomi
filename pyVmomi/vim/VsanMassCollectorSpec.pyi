# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.VsanMassCollectorPropertyParams import VsanMassCollectorPropertyParams

from pyVmomi.vim.VsanResourceConstraint import VsanResourceConstraint

from pyVmomi.vmodl.DynamicData import DynamicData

class VsanMassCollectorSpec(DynamicData):
   objects: list[ManagedObject] = []
   objectCollection: Optional[str] = None
   properties: list[str] = []
   propertiesParams: list[VsanMassCollectorPropertyParams] = []
   constraint: Optional[VsanResourceConstraint] = None
