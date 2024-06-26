# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.fault import OvfSystemFault

from pyVmomi.vim.vm.device import VirtualDevice

class OvfUnknownDevice(OvfSystemFault):
   device: Optional[VirtualDevice] = None
   vmName: str
