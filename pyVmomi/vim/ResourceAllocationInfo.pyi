# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import SharesInfo

from pyVmomi.vmodl import DynamicData

class ResourceAllocationInfo(DynamicData):
   reservation: Optional[long] = None
   expandableReservation: Optional[bool] = None
   limit: Optional[long] = None
   shares: Optional[SharesInfo] = None
   overheadLimit: Optional[long] = None
