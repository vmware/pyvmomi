# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.host.PciPassthruInfo import PciPassthruInfo

class SriovInfo(PciPassthruInfo):
   sriovEnabled: bool
   sriovCapable: bool
   sriovActive: bool
   numVirtualFunctionRequested: int
   numVirtualFunction: int
   maxVirtualFunctionSupported: int
