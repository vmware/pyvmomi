# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.vm import TargetInfo

class VgpuDeviceInfo(TargetInfo):
   deviceName: str
   deviceVendorId: long
   maxFbSizeInGib: long
   timeSlicedCapable: bool
   migCapable: bool
   computeProfileCapable: bool
   quadroProfileCapable: bool
