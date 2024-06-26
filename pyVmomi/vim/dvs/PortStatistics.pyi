# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class PortStatistics(DynamicData):
   packetsInMulticast: long
   packetsOutMulticast: long
   bytesInMulticast: long
   bytesOutMulticast: long
   packetsInUnicast: long
   packetsOutUnicast: long
   bytesInUnicast: long
   bytesOutUnicast: long
   packetsInBroadcast: long
   packetsOutBroadcast: long
   bytesInBroadcast: long
   bytesOutBroadcast: long
   packetsInDropped: long
   packetsOutDropped: long
   packetsInException: long
   packetsOutException: long
   bytesInFromPnic: Optional[long] = None
   bytesOutToPnic: Optional[long] = None
