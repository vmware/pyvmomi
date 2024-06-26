# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import AboutInfo
from pyVmomi.vim import Datastore
from pyVmomi.vim import Folder
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Network
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.host import ConnectInfo
from pyVmomi.vim.host import ConnectSpec

from pyVmomi.vim.option import OptionValue

from pyVmomi.vim.vm import ConfigOptionDescriptor

class Datacenter(ManagedEntity):
   class BasicConnectInfo(DynamicData):
      hostname: Optional[str] = None
      error: Optional[MethodFault] = None
      serverIp: Optional[str] = None
      numVm: Optional[int] = None
      numPoweredOnVm: Optional[int] = None
      hostProductInfo: Optional[AboutInfo] = None
      hardwareVendor: Optional[str] = None
      hardwareModel: Optional[str] = None

   class ConfigInfo(DynamicData):
      defaultHardwareVersionKey: Optional[str] = None
      maximumHardwareVersionKey: Optional[str] = None

   class ConfigSpec(DynamicData):
      defaultHardwareVersionKey: Optional[str] = None
      maximumHardwareVersionKey: Optional[str] = None

   @property
   def vmFolder(self) -> Folder: ...
   @property
   def hostFolder(self) -> Folder: ...
   @property
   def datastoreFolder(self) -> Folder: ...
   @property
   def networkFolder(self) -> Folder: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def configuration(self) -> ConfigInfo: ...

   def BatchQueryConnectInfo(self, hostSpecs: list[ConnectSpec]) -> list[BasicConnectInfo]: ...
   def QueryConnectionInfo(self, hostname: str, port: int, username: str, password: str, sslThumbprint: Optional[str]) -> ConnectInfo: ...
   def QueryConnectionInfoViaSpec(self, spec: ConnectSpec) -> ConnectInfo: ...
   def PowerOnVm(self, vm: list[VirtualMachine], option: list[OptionValue]) -> Task: ...
   def QueryConfigOptionDescriptor(self) -> list[ConfigOptionDescriptor]: ...
   def Reconfigure(self, spec: ConfigSpec, modify: bool) -> Task: ...
