# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl



class AliasManager(pyVmomi.VmomiSupport.ManagedObject):
   class GuestAuthSubject(pyVmomi.vmodl.DynamicData):
      pass

   class GuestAuthAnySubject(GuestAuthSubject):
      pass

   class GuestAuthNamedSubject(GuestAuthSubject):
      name: str

   class GuestAuthAliasInfo(pyVmomi.vmodl.DynamicData):
      subject: GuestAuthSubject
      comment: str

   class GuestAliases(pyVmomi.vmodl.DynamicData):
      base64Cert: str
      aliases: list[GuestAuthAliasInfo] = []

   class GuestMappedAliases(pyVmomi.vmodl.DynamicData):
      base64Cert: str
      username: str
      subjects: list[GuestAuthSubject] = []

   def AddAlias(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, username: str, mapCert: bool, base64Cert: str, aliasInfo: GuestAuthAliasInfo) -> None: ...
   def RemoveAlias(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, username: str, base64Cert: str, subject: GuestAuthSubject) -> None: ...
   def RemoveAliasByCert(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, username: str, base64Cert: str) -> None: ...
   def ListAliases(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, username: str) -> list[GuestAliases]: ...
   def ListMappedAliases(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication) -> list[GuestMappedAliases]: ...


class AuthManager(pyVmomi.VmomiSupport.ManagedObject):
   def ValidateCredentials(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication) -> None: ...
   def AcquireCredentials(self, vm: pyVmomi.vim.VirtualMachine, requestedAuth: GuestAuthentication, sessionID: _typing.Optional[pyVmomi.VmomiSupport.long]) -> GuestAuthentication: ...
   def ReleaseCredentials(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication) -> None: ...


class FileManager(pyVmomi.VmomiSupport.ManagedObject):
   class FileAttributes(pyVmomi.vmodl.DynamicData):
      modificationTime: _typing.Optional[_datetime.datetime] = None
      accessTime: _typing.Optional[_datetime.datetime] = None
      symlinkTarget: _typing.Optional[str] = None

   class PosixFileAttributes(FileAttributes):
      ownerId: _typing.Optional[int] = None
      groupId: _typing.Optional[int] = None
      permissions: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class WindowsFileAttributes(FileAttributes):
      hidden: _typing.Optional[bool] = None
      readOnly: _typing.Optional[bool] = None
      createTime: _typing.Optional[_datetime.datetime] = None

   class FileInfo(pyVmomi.vmodl.DynamicData):
      class FileType(pyVmomi.VmomiSupport.Enum):
         file: _typing.ClassVar['FileType'] = 'file'
         directory: _typing.ClassVar['FileType'] = 'directory'
         symlink: _typing.ClassVar['FileType'] = 'symlink'

      path: str
      type: str
      size: pyVmomi.VmomiSupport.long
      attributes: FileAttributes

   class ListFileInfo(pyVmomi.vmodl.DynamicData):
      files: list[FileInfo] = []
      remaining: int

   class FileTransferInformation(pyVmomi.vmodl.DynamicData):
      attributes: FileAttributes
      size: pyVmomi.VmomiSupport.long
      url: str

   def MakeDirectory(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, directoryPath: str, createParentDirectories: bool) -> None: ...
   def DeleteFile(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, filePath: str) -> None: ...
   def DeleteDirectory(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, directoryPath: str, recursive: bool) -> None: ...
   def MoveDirectory(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, srcDirectoryPath: str, dstDirectoryPath: str) -> None: ...
   def MoveFile(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, srcFilePath: str, dstFilePath: str, overwrite: bool) -> None: ...
   def CreateTemporaryFile(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, prefix: str, suffix: str, directoryPath: _typing.Optional[str]) -> str: ...
   def CreateTemporaryDirectory(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, prefix: str, suffix: str, directoryPath: _typing.Optional[str]) -> str: ...
   def ListFiles(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, filePath: str, index: _typing.Optional[int], maxResults: _typing.Optional[int], matchPattern: _typing.Optional[str]) -> ListFileInfo: ...
   def ChangeFileAttributes(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, guestFilePath: str, fileAttributes: FileAttributes) -> None: ...
   def InitiateFileTransferFromGuest(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, guestFilePath: str) -> FileTransferInformation: ...
   def InitiateFileTransferToGuest(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, guestFilePath: str, fileAttributes: FileAttributes, fileSize: pyVmomi.VmomiSupport.long, overwrite: bool) -> str: ...


class GuestAuthentication(pyVmomi.vmodl.DynamicData):
   interactiveSession: bool


class GuestOperationsManager(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def authManager(self) -> _typing.Optional[AuthManager]: ...
   @property
   def fileManager(self) -> _typing.Optional[FileManager]: ...
   @property
   def processManager(self) -> _typing.Optional[ProcessManager]: ...
   @property
   def guestWindowsRegistryManager(self) -> _typing.Optional[WindowsRegistryManager]: ...
   @property
   def aliasManager(self) -> _typing.Optional[AliasManager]: ...

class NamePasswordAuthentication(GuestAuthentication):
   username: str
   password: str


class ProcessManager(pyVmomi.VmomiSupport.ManagedObject):
   class ProgramSpec(pyVmomi.vmodl.DynamicData):
      programPath: str
      arguments: str
      workingDirectory: _typing.Optional[str] = None
      envVariables: list[str] = []

   class WindowsProgramSpec(ProgramSpec):
      startMinimized: bool

   class ProcessInfo(pyVmomi.vmodl.DynamicData):
      name: str
      pid: pyVmomi.VmomiSupport.long
      owner: str
      cmdLine: str
      startTime: _datetime.datetime
      endTime: _typing.Optional[_datetime.datetime] = None
      exitCode: _typing.Optional[int] = None

   def StartProgram(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, spec: ProgramSpec) -> pyVmomi.VmomiSupport.long: ...
   def ListProcesses(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, pids: list[pyVmomi.VmomiSupport.long]) -> list[ProcessInfo]: ...
   def TerminateProcess(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, pid: pyVmomi.VmomiSupport.long) -> None: ...
   def ReadEnvironmentVariable(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, names: list[str]) -> list[str]: ...


class SAMLTokenAuthentication(GuestAuthentication):
   token: str
   username: _typing.Optional[str] = None

class SSPIAuthentication(GuestAuthentication):
   sspiToken: str

class TicketedSessionAuthentication(GuestAuthentication):
   ticket: str


class WindowsRegistryManager(pyVmomi.VmomiSupport.ManagedObject):
   class RegistryKeyName(pyVmomi.vmodl.DynamicData):
      class RegistryKeyWowBitness(pyVmomi.VmomiSupport.Enum):
         WOWNative: _typing.ClassVar['RegistryKeyWowBitness'] = 'WOWNative'
         WOW32: _typing.ClassVar['RegistryKeyWowBitness'] = 'WOW32'
         WOW64: _typing.ClassVar['RegistryKeyWowBitness'] = 'WOW64'

      registryPath: str
      wowBitness: str

   class RegistryKey(pyVmomi.vmodl.DynamicData):
      keyName: RegistryKeyName
      classType: str
      lastWritten: _datetime.datetime

   class RegistryKeyRecord(pyVmomi.vmodl.DynamicData):
      key: RegistryKey
      fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

   class RegistryValueName(pyVmomi.vmodl.DynamicData):
      keyName: RegistryKeyName
      name: str

   class RegistryValueData(pyVmomi.vmodl.DynamicData):
      pass

   class RegistryValueDword(RegistryValueData):
      value: int

   class RegistryValueQword(RegistryValueData):
      value: pyVmomi.VmomiSupport.long

   class RegistryValueString(RegistryValueData):
      value: _typing.Optional[str] = None

   class RegistryValueExpandString(RegistryValueData):
      value: _typing.Optional[str] = None

   class RegistryValueMultiString(RegistryValueData):
      value: list[str] = []

   class RegistryValueBinary(RegistryValueData):
      value: _typing.Optional[pyVmomi.VmomiSupport.binary] = None

   class RegistryValue(pyVmomi.vmodl.DynamicData):
      name: RegistryValueName
      data: RegistryValueData

   def CreateRegistryKey(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, keyName: RegistryKeyName, isVolatile: bool, classType: _typing.Optional[str]) -> None: ...
   def ListRegistryKeys(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, keyName: RegistryKeyName, recursive: bool, matchPattern: _typing.Optional[str]) -> list[RegistryKeyRecord]: ...
   def DeleteRegistryKey(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, keyName: RegistryKeyName, recursive: bool) -> None: ...
   def SetRegistryValue(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, value: RegistryValue) -> None: ...
   def ListRegistryValues(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, keyName: RegistryKeyName, expandStrings: bool, matchPattern: _typing.Optional[str]) -> list[RegistryValue]: ...
   def DeleteRegistryValue(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, valueName: RegistryValueName) -> None: ...
