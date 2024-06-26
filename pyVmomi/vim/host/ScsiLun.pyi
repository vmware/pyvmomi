# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import byte

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import Device

class ScsiLun(Device):
   class ScsiLunType(Enum):
      disk: ClassVar['ScsiLunType'] = 'disk'
      tape: ClassVar['ScsiLunType'] = 'tape'
      printer: ClassVar['ScsiLunType'] = 'printer'
      processor: ClassVar['ScsiLunType'] = 'processor'
      worm: ClassVar['ScsiLunType'] = 'worm'
      cdrom: ClassVar['ScsiLunType'] = 'cdrom'
      scanner: ClassVar['ScsiLunType'] = 'scanner'
      opticalDevice: ClassVar['ScsiLunType'] = 'opticalDevice'
      mediaChanger: ClassVar['ScsiLunType'] = 'mediaChanger'
      communications: ClassVar['ScsiLunType'] = 'communications'
      storageArrayController: ClassVar['ScsiLunType'] = 'storageArrayController'
      enclosure: ClassVar['ScsiLunType'] = 'enclosure'
      unknown: ClassVar['ScsiLunType'] = 'unknown'

   class DeviceProtocol(Enum):
      NVMe: ClassVar['DeviceProtocol'] = 'NVMe'
      SCSI: ClassVar['DeviceProtocol'] = 'SCSI'

   class Capabilities(DynamicData):
      updateDisplayNameSupported: bool

   class DurableName(DynamicData):
      namespace: str
      namespaceId: byte
      data: list[byte] = []

   class State(Enum):
      unknownState: ClassVar['State'] = 'unknownState'
      ok: ClassVar['State'] = 'ok'
      error: ClassVar['State'] = 'error'
      off: ClassVar['State'] = 'off'
      quiesced: ClassVar['State'] = 'quiesced'
      degraded: ClassVar['State'] = 'degraded'
      lostCommunication: ClassVar['State'] = 'lostCommunication'
      timeout: ClassVar['State'] = 'timeout'

   class DescriptorQuality(Enum):
      highQuality: ClassVar['DescriptorQuality'] = 'highQuality'
      mediumQuality: ClassVar['DescriptorQuality'] = 'mediumQuality'
      lowQuality: ClassVar['DescriptorQuality'] = 'lowQuality'
      unknownQuality: ClassVar['DescriptorQuality'] = 'unknownQuality'

   class Descriptor(DynamicData):
      quality: str
      id: str

   class VStorageSupportStatus(Enum):
      vStorageSupported: ClassVar['VStorageSupportStatus'] = 'vStorageSupported'
      vStorageUnsupported: ClassVar['VStorageSupportStatus'] = 'vStorageUnsupported'
      vStorageUnknown: ClassVar['VStorageSupportStatus'] = 'vStorageUnknown'

   class LunReservationStatus(Enum):
      LUN_RESERVED_UNKNOWN: ClassVar['LunReservationStatus'] = 'LUN_RESERVED_UNKNOWN'
      LUN_RESERVED_YES: ClassVar['LunReservationStatus'] = 'LUN_RESERVED_YES'
      LUN_RESERVED_NO: ClassVar['LunReservationStatus'] = 'LUN_RESERVED_NO'
      LUN_RESERVED_NOT_SUPPORTED: ClassVar['LunReservationStatus'] = 'LUN_RESERVED_NOT_SUPPORTED'

   key: Optional[str] = None
   uuid: str
   descriptor: list[Descriptor] = []
   canonicalName: Optional[str] = None
   displayName: Optional[str] = None
   lunType: str
   vendor: Optional[str] = None
   model: Optional[str] = None
   revision: Optional[str] = None
   scsiLevel: Optional[int] = None
   serialNumber: Optional[str] = None
   durableName: Optional[DurableName] = None
   alternateName: list[DurableName] = []
   standardInquiry: list[byte] = []
   queueDepth: Optional[int] = None
   operationalState: list[str] = []
   capabilities: Optional[Capabilities] = None
   vStorageSupport: Optional[str] = None
   protocolEndpoint: Optional[bool] = None
   perenniallyReserved: Optional[bool] = None
   clusteredVmdkSupported: Optional[bool] = None
   applicationProtocol: Optional[str] = None
   dispersedNs: Optional[bool] = None
   deviceReservation: Optional[str] = None
