# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vmodl



class DatastoreSpaceStatistics(pyVmomi.vmodl.DynamicData):
   """
   Space stats for datastore
   
   Attributes:
       profileId: Capability profile id.
           
           It is null when the statistics are for the entire
           datastore.
       physicalTotalInMB: Total physical space in MB.
       physicalFreeInMB: Total physical free space in MB.
       physicalUsedInMB: Used physical storage space in MB.
       logicalLimitInMB: Logical space limit set by the storage admin in MB.
           
           Omitted if there is no Logical space limit.
       logicalFreeInMB: Free logical storage space in MB.
       logicalUsedInMB: Used logical storage space in MB.
   """
   profileId: _typing.Optional[str] = None
   physicalTotalInMB: pyVmomi.VmomiSupport.long
   physicalFreeInMB: pyVmomi.VmomiSupport.long
   physicalUsedInMB: pyVmomi.VmomiSupport.long
   logicalLimitInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   logicalFreeInMB: pyVmomi.VmomiSupport.long
   logicalUsedInMB: pyVmomi.VmomiSupport.long
