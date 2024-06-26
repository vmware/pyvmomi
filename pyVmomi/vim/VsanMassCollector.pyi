# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import VsanMassCollectorSpec

from pyVmomi.vmodl.query import PropertyCollector

class VsanMassCollector(ManagedObject):
   def VsanRetrieveProperties(self, massCollectorSpecs: list[VsanMassCollectorSpec]) -> list[PropertyCollector.ObjectContent]: ...
