# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vm.customization.Password import Password

class Identification(DynamicData):
   joinWorkgroup: Optional[str] = None
   joinDomain: Optional[str] = None
   domainAdmin: Optional[str] = None
   domainAdminPassword: Optional[Password] = None
   domainOU: Optional[str] = None
