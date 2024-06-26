# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import Datastore
from pyVmomi.vim import Description

from pyVmomi.vmodl import DynamicData

class VirtualDevice(DynamicData):
   class BackingInfo(DynamicData):
      pass

   class FileBackingInfo(BackingInfo):
      fileName: str
      datastore: Optional[Datastore] = None
      backingObjectId: Optional[str] = None

   class DeviceBackingInfo(BackingInfo):
      deviceName: str
      useAutoDetect: Optional[bool] = None

   class RemoteDeviceBackingInfo(BackingInfo):
      deviceName: str
      useAutoDetect: Optional[bool] = None

   class PipeBackingInfo(BackingInfo):
      pipeName: str

   class URIBackingInfo(BackingInfo):
      serviceURI: str
      direction: str
      proxyURI: Optional[str] = None

   class ConnectInfo(DynamicData):
      class Status(Enum):
         ok: ClassVar['Status'] = 'ok'
         recoverableError: ClassVar['Status'] = 'recoverableError'
         unrecoverableError: ClassVar['Status'] = 'unrecoverableError'
         untried: ClassVar['Status'] = 'untried'

      class MigrateConnectOp(Enum):
         connect: ClassVar['MigrateConnectOp'] = 'connect'
         disconnect: ClassVar['MigrateConnectOp'] = 'disconnect'
         unset: ClassVar['MigrateConnectOp'] = 'unset'

      migrateConnect: Optional[str] = None
      startConnected: bool
      allowGuestControl: bool
      connected: bool
      status: Optional[str] = None

   class BusSlotInfo(DynamicData):
      pass

   class PciBusSlotInfo(BusSlotInfo):
      pciSlotNumber: int

   class DeviceGroupInfo(DynamicData):
      groupInstanceKey: int
      sequenceId: int

   key: int
   deviceInfo: Optional[Description] = None
   backing: Optional[BackingInfo] = None
   connectable: Optional[ConnectInfo] = None
   slotInfo: Optional[BusSlotInfo] = None
   controllerKey: Optional[int] = None
   unitNumber: Optional[int] = None
   numaNode: Optional[int] = None
   deviceGroupInfo: Optional[DeviceGroupInfo] = None
