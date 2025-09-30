# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vmodl.DynamicData import DynamicData

class PortConnectee(DynamicData):
   class ConnecteeType(Enum):
      pnic: ClassVar['ConnecteeType'] = 'pnic'
      vmVnic: ClassVar['ConnecteeType'] = 'vmVnic'
      hostConsoleVnic: ClassVar['ConnecteeType'] = 'hostConsoleVnic'
      hostVmkVnic: ClassVar['ConnecteeType'] = 'hostVmkVnic'
      systemCrxVnic: ClassVar['ConnecteeType'] = 'systemCrxVnic'

   connectedEntity: Optional[ManagedEntity] = None
   nicKey: Optional[str] = None
   type: Optional[str] = None
   addressHint: Optional[str] = None
