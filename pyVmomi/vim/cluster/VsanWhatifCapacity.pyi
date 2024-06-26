# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm import ProfileSpec

class VsanWhatifCapacity(DynamicData):
   totalWhatifCapacityB: long
   freeWhatifCapacityB: long
   storagePolicy: ProfileSpec
   isSatisfiable: bool
