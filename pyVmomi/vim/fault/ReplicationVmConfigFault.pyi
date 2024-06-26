# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.fault import ReplicationConfigFault

class ReplicationVmConfigFault(ReplicationConfigFault):
   class ReasonForFault(Enum):
      incompatibleHwVersion: ClassVar['ReasonForFault'] = 'incompatibleHwVersion'
      invalidVmReplicationId: ClassVar['ReasonForFault'] = 'invalidVmReplicationId'
      invalidGenerationNumber: ClassVar['ReasonForFault'] = 'invalidGenerationNumber'
      outOfBoundsRpoValue: ClassVar['ReasonForFault'] = 'outOfBoundsRpoValue'
      invalidDestinationIpAddress: ClassVar['ReasonForFault'] = 'invalidDestinationIpAddress'
      invalidDestinationPort: ClassVar['ReasonForFault'] = 'invalidDestinationPort'
      invalidExtraVmOptions: ClassVar['ReasonForFault'] = 'invalidExtraVmOptions'
      staleGenerationNumber: ClassVar['ReasonForFault'] = 'staleGenerationNumber'
      reconfigureVmReplicationIdNotAllowed: ClassVar['ReasonForFault'] = 'reconfigureVmReplicationIdNotAllowed'
      cannotRetrieveVmReplicationConfiguration: ClassVar['ReasonForFault'] = 'cannotRetrieveVmReplicationConfiguration'
      replicationAlreadyEnabled: ClassVar['ReasonForFault'] = 'replicationAlreadyEnabled'
      invalidPriorConfiguration: ClassVar['ReasonForFault'] = 'invalidPriorConfiguration'
      replicationNotEnabled: ClassVar['ReasonForFault'] = 'replicationNotEnabled'
      replicationConfigurationFailed: ClassVar['ReasonForFault'] = 'replicationConfigurationFailed'
      encryptedVm: ClassVar['ReasonForFault'] = 'encryptedVm'
      invalidThumbprint: ClassVar['ReasonForFault'] = 'invalidThumbprint'
      incompatibleDevice: ClassVar['ReasonForFault'] = 'incompatibleDevice'

   reason: Optional[str] = None
   vmRef: Optional[VirtualMachine] = None
