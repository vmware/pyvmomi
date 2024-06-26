# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.host import PciPassthruInfo

class SriovInfo(PciPassthruInfo):
   sriovEnabled: bool
   sriovCapable: bool
   sriovActive: bool
   numVirtualFunctionRequested: int
   numVirtualFunction: int
   maxVirtualFunctionSupported: int
