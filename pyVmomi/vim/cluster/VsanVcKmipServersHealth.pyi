# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.host import VsanKmsHealth

class VsanVcKmipServersHealth(DynamicData):
   health: Optional[str] = None
   error: Optional[MethodFault] = None
   kmsProviderId: Optional[str] = None
   kmsHealth: list[VsanKmsHealth] = []
   clientCertHealth: Optional[str] = None
   clientCertExpireDate: Optional[datetime] = None
   isAwsKms: Optional[bool] = None
   cmkHealth: Optional[str] = None
   kekExpireHealth: Optional[str] = None
   kekExpireDate: Optional[datetime] = None
   hostKeyExpireHealth: Optional[str] = None
   hostKeyExpireDate: Optional[datetime] = None
