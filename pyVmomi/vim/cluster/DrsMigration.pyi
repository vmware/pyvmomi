# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import HostSystem
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

class DrsMigration(DynamicData):
   key: str
   time: datetime
   vm: VirtualMachine
   cpuLoad: Optional[int] = None
   memoryLoad: Optional[long] = None
   source: HostSystem
   sourceCpuLoad: Optional[int] = None
   sourceMemoryLoad: Optional[long] = None
   destination: HostSystem
   destinationCpuLoad: Optional[int] = None
   destinationMemoryLoad: Optional[long] = None
