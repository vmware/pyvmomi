# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.fault import ReplicationConfigFault

class ReplicationDiskConfigFault(ReplicationConfigFault):
   class ReasonForFault(Enum):
      diskNotFound: ClassVar['ReasonForFault'] = 'diskNotFound'
      diskTypeNotSupported: ClassVar['ReasonForFault'] = 'diskTypeNotSupported'
      invalidDiskKey: ClassVar['ReasonForFault'] = 'invalidDiskKey'
      invalidDiskReplicationId: ClassVar['ReasonForFault'] = 'invalidDiskReplicationId'
      duplicateDiskReplicationId: ClassVar['ReasonForFault'] = 'duplicateDiskReplicationId'
      invalidPersistentFilePath: ClassVar['ReasonForFault'] = 'invalidPersistentFilePath'
      reconfigureDiskReplicationIdNotAllowed: ClassVar['ReasonForFault'] = 'reconfigureDiskReplicationIdNotAllowed'

   reason: Optional[str] = None
   vmRef: Optional[VirtualMachine] = None
   key: Optional[int] = None
