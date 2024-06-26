# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.option import LongOption

from pyVmomi.vim.vm.device import VirtualDeviceOption

class VirtualNVDIMMOption(VirtualDeviceOption):
   capacityInMB: LongOption
   growable: bool
   hotGrowable: bool
   granularityInMB: long
