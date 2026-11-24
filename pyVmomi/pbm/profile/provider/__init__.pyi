# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vmodl



class DatastoreSpaceStatistics(pyVmomi.vmodl.DynamicData):
   profileId: _typing.Optional[str] = None
   physicalTotalInMB: pyVmomi.VmomiSupport.long
   physicalFreeInMB: pyVmomi.VmomiSupport.long
   physicalUsedInMB: pyVmomi.VmomiSupport.long
   logicalLimitInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   logicalFreeInMB: pyVmomi.VmomiSupport.long
   logicalUsedInMB: pyVmomi.VmomiSupport.long
