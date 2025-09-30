# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.AuthorizationManager import AuthorizationManager

from pyVmomi.vmodl.DynamicData import DynamicData

class SecuritySpec(DynamicData):
   adminPassword: Optional[str] = None
   removePermission: list[AuthorizationManager.Permission] = []
   addPermission: list[AuthorizationManager.Permission] = []
