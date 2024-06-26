# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import HostSystem
from pyVmomi.vim import VasaStorageArray
from pyVmomi.vim import VimVasaProviderInfo

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import FileSystemVolume
from pyVmomi.vim.host import ProtocolEndpoint
from pyVmomi.vim.host import VvolNQN

class VvolVolume(FileSystemVolume):
   class Specification(DynamicData):
      maxSizeInMB: long
      volumeName: str
      vasaProviderInfo: list[VimVasaProviderInfo] = []
      storageArray: list[VasaStorageArray] = []
      uuid: str
      stretched: Optional[bool] = None

   class HostProtocolEndpoint(DynamicData):
      key: HostSystem
      protocolEndpoint: list[ProtocolEndpoint] = []

   class HostVvolNQN(DynamicData):
      host: Optional[HostSystem] = None
      vvolNQN: list[VvolNQN] = []

   scId: str
   hostPE: list[HostProtocolEndpoint] = []
   hostVvolNQN: list[HostVvolNQN] = []
   vasaProviderInfo: list[VimVasaProviderInfo] = []
   storageArray: list[VasaStorageArray] = []
   protocolEndpointType: Optional[str] = None
   vvolNQNFieldsAvailable: Optional[bool] = None
   stretched: Optional[bool] = None
