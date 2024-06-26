# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.dvs import HostMember

from pyVmomi.vim.event import HostEvent

class DvsHealthStatusChangeEvent(HostEvent):
   switchUuid: str
   healthResult: Optional[HostMember.HealthCheckResult] = None
