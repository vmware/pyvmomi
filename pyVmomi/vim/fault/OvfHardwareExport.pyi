# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.fault import OvfExport

from pyVmomi.vim.vm.device import VirtualDevice

class OvfHardwareExport(OvfExport):
   device: Optional[VirtualDevice] = None
   vmPath: str
