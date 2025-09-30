# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.fault.OvfSystemFault import OvfSystemFault

from pyVmomi.vim.vm.device.VirtualDevice import VirtualDevice

class OvfUnknownDevice(OvfSystemFault):
   device: Optional[VirtualDevice] = None
   vmName: str
