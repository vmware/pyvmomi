# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import AuthorizationManager

from pyVmomi.vmodl import DynamicData

class SecuritySpec(DynamicData):
   adminPassword: Optional[str] = None
   removePermission: list[AuthorizationManager.Permission] = []
   addPermission: list[AuthorizationManager.Permission] = []
