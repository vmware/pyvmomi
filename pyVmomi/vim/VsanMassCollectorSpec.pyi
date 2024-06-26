# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import VsanMassCollectorPropertyParams
from pyVmomi.vim import VsanResourceConstraint

from pyVmomi.vmodl import DynamicData

class VsanMassCollectorSpec(DynamicData):
   objects: list[ManagedObject] = []
   objectCollection: Optional[str] = None
   properties: list[str] = []
   propertiesParams: list[VsanMassCollectorPropertyParams] = []
   constraint: Optional[VsanResourceConstraint] = None
