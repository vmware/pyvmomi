# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.fault import ReplicationFault

class ReplicationVmFault(ReplicationFault):
   class ReasonForFault(Enum):
      notConfigured: ClassVar['ReasonForFault'] = 'notConfigured'
      poweredOff: ClassVar['ReasonForFault'] = 'poweredOff'
      suspended: ClassVar['ReasonForFault'] = 'suspended'
      poweredOn: ClassVar['ReasonForFault'] = 'poweredOn'
      offlineReplicating: ClassVar['ReasonForFault'] = 'offlineReplicating'
      invalidState: ClassVar['ReasonForFault'] = 'invalidState'
      invalidInstanceId: ClassVar['ReasonForFault'] = 'invalidInstanceId'
      closeDiskError: ClassVar['ReasonForFault'] = 'closeDiskError'
      groupExist: ClassVar['ReasonForFault'] = 'groupExist'

   reason: str
   state: Optional[str] = None
   instanceId: Optional[str] = None
   vm: VirtualMachine
