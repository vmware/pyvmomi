# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import MethodFault
from pyVmomi.vmodl import RuntimeFault

class UnexpectedFault(RuntimeFault):
   faultName: type
   fault: Optional[MethodFault] = None
