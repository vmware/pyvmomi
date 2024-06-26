# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import binary
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.vm.guest import GuestAuthentication

class WindowsRegistryManager(ManagedObject):
   class RegistryKeyName(DynamicData):
      class RegistryKeyWowBitness(Enum):
         WOWNative: ClassVar['RegistryKeyWowBitness'] = 'WOWNative'
         WOW32: ClassVar['RegistryKeyWowBitness'] = 'WOW32'
         WOW64: ClassVar['RegistryKeyWowBitness'] = 'WOW64'

      registryPath: str
      wowBitness: str

   class RegistryKey(DynamicData):
      keyName: RegistryKeyName
      classType: str
      lastWritten: datetime

   class RegistryKeyRecord(DynamicData):
      key: RegistryKey
      fault: Optional[MethodFault] = None

   class RegistryValueName(DynamicData):
      keyName: RegistryKeyName
      name: str

   class RegistryValueData(DynamicData):
      pass

   class RegistryValueDword(RegistryValueData):
      value: int

   class RegistryValueQword(RegistryValueData):
      value: long

   class RegistryValueString(RegistryValueData):
      value: Optional[str] = None

   class RegistryValueExpandString(RegistryValueData):
      value: Optional[str] = None

   class RegistryValueMultiString(RegistryValueData):
      value: list[str] = []

   class RegistryValueBinary(RegistryValueData):
      value: Optional[binary] = None

   class RegistryValue(DynamicData):
      name: RegistryValueName
      data: RegistryValueData

   def CreateRegistryKey(self, vm: VirtualMachine, auth: GuestAuthentication, keyName: RegistryKeyName, isVolatile: bool, classType: Optional[str]) -> NoReturn: ...
   def ListRegistryKeys(self, vm: VirtualMachine, auth: GuestAuthentication, keyName: RegistryKeyName, recursive: bool, matchPattern: Optional[str]) -> list[RegistryKeyRecord]: ...
   def DeleteRegistryKey(self, vm: VirtualMachine, auth: GuestAuthentication, keyName: RegistryKeyName, recursive: bool) -> NoReturn: ...
   def SetRegistryValue(self, vm: VirtualMachine, auth: GuestAuthentication, value: RegistryValue) -> NoReturn: ...
   def ListRegistryValues(self, vm: VirtualMachine, auth: GuestAuthentication, keyName: RegistryKeyName, expandStrings: bool, matchPattern: Optional[str]) -> list[RegistryValue]: ...
   def DeleteRegistryValue(self, vm: VirtualMachine, auth: GuestAuthentication, valueName: RegistryValueName) -> NoReturn: ...
