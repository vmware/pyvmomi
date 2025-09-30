# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.ComputeResource import ComputeResource

from pyVmomi.vmodl.fault.NotEnoughLicenses import NotEnoughLicenses

class FailToEnableSPBM(NotEnoughLicenses):
   cs: ComputeResource
   csName: str
   hostLicenseStates: list[ComputeResource.HostSPBMLicenseInfo] = []
