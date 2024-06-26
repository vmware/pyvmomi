# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import NvmeTransportParameters

class NvmeDiscoveryLog(DynamicData):
   class SubsystemType(Enum):
      discovery: ClassVar['SubsystemType'] = 'discovery'
      nvm: ClassVar['SubsystemType'] = 'nvm'

   class TransportRequirements(Enum):
      secureChannelRequired: ClassVar['TransportRequirements'] = 'secureChannelRequired'
      secureChannelNotRequired: ClassVar['TransportRequirements'] = 'secureChannelNotRequired'
      requirementsNotSpecified: ClassVar['TransportRequirements'] = 'requirementsNotSpecified'

   class Entry(DynamicData):
      subnqn: str
      subsystemType: str
      subsystemPortId: int
      controllerId: int
      adminQueueMaxSize: int
      transportParameters: NvmeTransportParameters
      transportRequirements: str
      connected: bool

   entry: list[Entry] = []
   complete: bool
