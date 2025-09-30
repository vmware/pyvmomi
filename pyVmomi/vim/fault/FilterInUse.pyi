# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.fault.ResourceInUse import ResourceInUse

from pyVmomi.vim.vm.device.VirtualDiskId import VirtualDiskId

class FilterInUse(ResourceInUse):
   disk: list[VirtualDiskId] = []
