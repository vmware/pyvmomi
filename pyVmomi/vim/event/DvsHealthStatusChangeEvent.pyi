# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.dvs.HostMember import HostMember

from pyVmomi.vim.event.HostEvent import HostEvent

class DvsHealthStatusChangeEvent(HostEvent):
   switchUuid: str
   healthResult: Optional[HostMember.HealthCheckResult] = None
