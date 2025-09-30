# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vim.fault.VirtualHardwareCompatibilityIssue import VirtualHardwareCompatibilityIssue

from pyVmomi.vim.vm.FeatureRequirement import FeatureRequirement

class FeatureRequirementsNotMet(VirtualHardwareCompatibilityIssue):
   featureRequirement: list[FeatureRequirement] = []
   vm: Optional[VirtualMachine] = None
   host: Optional[HostSystem] = None
