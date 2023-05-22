from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType, binary, long


class AliasManager(ManagedObject):
    def AddAlias(self, vm: vim.VirtualMachine, auth: GuestAuthentication, username: str, mapCert: bool, base64Cert: str, aliasInfo: AliasManager.GuestAuthAliasInfo) -> NoneType: ...
    def RemoveAlias(self, vm: vim.VirtualMachine, auth: GuestAuthentication, username: str, base64Cert: str, subject: AliasManager.GuestAuthSubject) -> NoneType: ...
    def RemoveAliasByCert(self, vm: vim.VirtualMachine, auth: GuestAuthentication, username: str, base64Cert: str) -> NoneType: ...
    def ListAliases(self, vm: vim.VirtualMachine, auth: GuestAuthentication, username: str) -> List[AliasManager.GuestAliases]: ...
    def ListMappedAliases(self, vm: vim.VirtualMachine, auth: GuestAuthentication) -> List[AliasManager.GuestMappedAliases]: ...


    class GuestAliases(vmodl.DynamicData):
        @property
        def base64Cert(self) -> str: ...
        @base64Cert.setter
        def base64Cert(self, value: str):
            self._base64Cert = value
        @property
        def aliases(self) -> List[AliasManager.GuestAuthAliasInfo]: ...
        @aliases.setter
        def aliases(self, value: List[AliasManager.GuestAuthAliasInfo]):
            self._aliases = value


    class GuestAuthAliasInfo(vmodl.DynamicData):
        @property
        def subject(self) -> AliasManager.GuestAuthSubject: ...
        @subject.setter
        def subject(self, value: AliasManager.GuestAuthSubject):
            self._subject = value
        @property
        def comment(self) -> str: ...
        @comment.setter
        def comment(self, value: str):
            self._comment = value


    class GuestAuthAnySubject(AliasManager.GuestAuthSubject): ...


    class GuestAuthNamedSubject(AliasManager.GuestAuthSubject):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value


    class GuestAuthSubject(vmodl.DynamicData): ...


    class GuestMappedAliases(vmodl.DynamicData):
        @property
        def base64Cert(self) -> str: ...
        @base64Cert.setter
        def base64Cert(self, value: str):
            self._base64Cert = value
        @property
        def username(self) -> str: ...
        @username.setter
        def username(self, value: str):
            self._username = value
        @property
        def subjects(self) -> List[AliasManager.GuestAuthSubject]: ...
        @subjects.setter
        def subjects(self, value: List[AliasManager.GuestAuthSubject]):
            self._subjects = value


class AuthManager(ManagedObject):
    def ValidateCredentials(self, vm: vim.VirtualMachine, auth: GuestAuthentication) -> NoneType: ...
    def AcquireCredentials(self, vm: vim.VirtualMachine, requestedAuth: GuestAuthentication, sessionID: long) -> GuestAuthentication: ...
    def ReleaseCredentials(self, vm: vim.VirtualMachine, auth: GuestAuthentication) -> NoneType: ...


class FileManager(ManagedObject):
    def MakeDirectory(self, vm: vim.VirtualMachine, auth: GuestAuthentication, directoryPath: str, createParentDirectories: bool) -> NoneType: ...
    def DeleteFile(self, vm: vim.VirtualMachine, auth: GuestAuthentication, filePath: str) -> NoneType: ...
    def DeleteDirectory(self, vm: vim.VirtualMachine, auth: GuestAuthentication, directoryPath: str, recursive: bool) -> NoneType: ...
    def MoveDirectory(self, vm: vim.VirtualMachine, auth: GuestAuthentication, srcDirectoryPath: str, dstDirectoryPath: str) -> NoneType: ...
    def MoveFile(self, vm: vim.VirtualMachine, auth: GuestAuthentication, srcFilePath: str, dstFilePath: str, overwrite: bool) -> NoneType: ...
    def CreateTemporaryFile(self, vm: vim.VirtualMachine, auth: GuestAuthentication, prefix: str, suffix: str, directoryPath: str) -> str: ...
    def CreateTemporaryDirectory(self, vm: vim.VirtualMachine, auth: GuestAuthentication, prefix: str, suffix: str, directoryPath: str) -> str: ...
    def ListFiles(self, vm: vim.VirtualMachine, auth: GuestAuthentication, filePath: str, index: int, maxResults: int, matchPattern: str) -> FileManager.ListFileInfo: ...
    def ChangeFileAttributes(self, vm: vim.VirtualMachine, auth: GuestAuthentication, guestFilePath: str, fileAttributes: FileManager.FileAttributes) -> NoneType: ...
    def InitiateFileTransferFromGuest(self, vm: vim.VirtualMachine, auth: GuestAuthentication, guestFilePath: str) -> FileManager.FileTransferInformation: ...
    def InitiateFileTransferToGuest(self, vm: vim.VirtualMachine, auth: GuestAuthentication, guestFilePath: str, fileAttributes: FileManager.FileAttributes, fileSize: long, overwrite: bool) -> str: ...


    class FileAttributes(vmodl.DynamicData):
        @property
        def modificationTime(self) -> datetime: ...
        @modificationTime.setter
        def modificationTime(self, value: datetime):
            self._modificationTime = value
        @property
        def accessTime(self) -> datetime: ...
        @accessTime.setter
        def accessTime(self, value: datetime):
            self._accessTime = value
        @property
        def symlinkTarget(self) -> str: ...
        @symlinkTarget.setter
        def symlinkTarget(self, value: str):
            self._symlinkTarget = value


    class FileInfo(vmodl.DynamicData):
        @property
        def path(self) -> str: ...
        @path.setter
        def path(self, value: str):
            self._path = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def size(self) -> long: ...
        @size.setter
        def size(self, value: long):
            self._size = value
        @property
        def attributes(self) -> FileManager.FileAttributes: ...
        @attributes.setter
        def attributes(self, value: FileManager.FileAttributes):
            self._attributes = value


        class FileType(Enum):
            file = "file"
            directory = "directory"
            symlink = "symlink"


    class FileTransferInformation(vmodl.DynamicData):
        @property
        def attributes(self) -> FileManager.FileAttributes: ...
        @attributes.setter
        def attributes(self, value: FileManager.FileAttributes):
            self._attributes = value
        @property
        def size(self) -> long: ...
        @size.setter
        def size(self, value: long):
            self._size = value
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value


    class ListFileInfo(vmodl.DynamicData):
        @property
        def files(self) -> List[FileManager.FileInfo]: ...
        @files.setter
        def files(self, value: List[FileManager.FileInfo]):
            self._files = value
        @property
        def remaining(self) -> int: ...
        @remaining.setter
        def remaining(self, value: int):
            self._remaining = value


    class PosixFileAttributes(FileManager.FileAttributes):
        @property
        def ownerId(self) -> int: ...
        @ownerId.setter
        def ownerId(self, value: int):
            self._ownerId = value
        @property
        def groupId(self) -> int: ...
        @groupId.setter
        def groupId(self, value: int):
            self._groupId = value
        @property
        def permissions(self) -> long: ...
        @permissions.setter
        def permissions(self, value: long):
            self._permissions = value


    class WindowsFileAttributes(FileManager.FileAttributes):
        @property
        def hidden(self) -> bool: ...
        @hidden.setter
        def hidden(self, value: bool):
            self._hidden = value
        @property
        def readOnly(self) -> bool: ...
        @readOnly.setter
        def readOnly(self, value: bool):
            self._readOnly = value
        @property
        def createTime(self) -> datetime: ...
        @createTime.setter
        def createTime(self, value: datetime):
            self._createTime = value


class GuestOperationsManager(ManagedObject):
    @property
    def authManager(self) -> AuthManager: ...
    @property
    def fileManager(self) -> FileManager: ...
    @property
    def processManager(self) -> ProcessManager: ...
    @property
    def guestWindowsRegistryManager(self) -> WindowsRegistryManager: ...
    @property
    def aliasManager(self) -> AliasManager: ...


class ProcessManager(ManagedObject):
    def StartProgram(self, vm: vim.VirtualMachine, auth: GuestAuthentication, spec: ProcessManager.ProgramSpec) -> long: ...
    def ListProcesses(self, vm: vim.VirtualMachine, auth: GuestAuthentication, pids: List[long]) -> List[ProcessManager.ProcessInfo]: ...
    def TerminateProcess(self, vm: vim.VirtualMachine, auth: GuestAuthentication, pid: long) -> NoneType: ...
    def ReadEnvironmentVariable(self, vm: vim.VirtualMachine, auth: GuestAuthentication, names: List[str]) -> List[str]: ...


    class ProcessInfo(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def pid(self) -> long: ...
        @pid.setter
        def pid(self, value: long):
            self._pid = value
        @property
        def owner(self) -> str: ...
        @owner.setter
        def owner(self, value: str):
            self._owner = value
        @property
        def cmdLine(self) -> str: ...
        @cmdLine.setter
        def cmdLine(self, value: str):
            self._cmdLine = value
        @property
        def startTime(self) -> datetime: ...
        @startTime.setter
        def startTime(self, value: datetime):
            self._startTime = value
        @property
        def endTime(self) -> datetime: ...
        @endTime.setter
        def endTime(self, value: datetime):
            self._endTime = value
        @property
        def exitCode(self) -> int: ...
        @exitCode.setter
        def exitCode(self, value: int):
            self._exitCode = value


    class ProgramSpec(vmodl.DynamicData):
        @property
        def programPath(self) -> str: ...
        @programPath.setter
        def programPath(self, value: str):
            self._programPath = value
        @property
        def arguments(self) -> str: ...
        @arguments.setter
        def arguments(self, value: str):
            self._arguments = value
        @property
        def workingDirectory(self) -> str: ...
        @workingDirectory.setter
        def workingDirectory(self, value: str):
            self._workingDirectory = value
        @property
        def envVariables(self) -> List[str]: ...
        @envVariables.setter
        def envVariables(self, value: List[str]):
            self._envVariables = value


    class WindowsProgramSpec(ProcessManager.ProgramSpec):
        @property
        def startMinimized(self) -> bool: ...
        @startMinimized.setter
        def startMinimized(self, value: bool):
            self._startMinimized = value


class WindowsRegistryManager(ManagedObject):
    def CreateRegistryKey(self, vm: vim.VirtualMachine, auth: GuestAuthentication, keyName: WindowsRegistryManager.RegistryKeyName, isVolatile: bool, classType: str) -> NoneType: ...
    def ListRegistryKeys(self, vm: vim.VirtualMachine, auth: GuestAuthentication, keyName: WindowsRegistryManager.RegistryKeyName, recursive: bool, matchPattern: str) -> List[WindowsRegistryManager.RegistryKeyRecord]: ...
    def DeleteRegistryKey(self, vm: vim.VirtualMachine, auth: GuestAuthentication, keyName: WindowsRegistryManager.RegistryKeyName, recursive: bool) -> NoneType: ...
    def SetRegistryValue(self, vm: vim.VirtualMachine, auth: GuestAuthentication, value: WindowsRegistryManager.RegistryValue) -> NoneType: ...
    def ListRegistryValues(self, vm: vim.VirtualMachine, auth: GuestAuthentication, keyName: WindowsRegistryManager.RegistryKeyName, expandStrings: bool, matchPattern: str) -> List[WindowsRegistryManager.RegistryValue]: ...
    def DeleteRegistryValue(self, vm: vim.VirtualMachine, auth: GuestAuthentication, valueName: WindowsRegistryManager.RegistryValueName) -> NoneType: ...


    class RegistryKey(vmodl.DynamicData):
        @property
        def keyName(self) -> WindowsRegistryManager.RegistryKeyName: ...
        @keyName.setter
        def keyName(self, value: WindowsRegistryManager.RegistryKeyName):
            self._keyName = value
        @property
        def classType(self) -> str: ...
        @classType.setter
        def classType(self, value: str):
            self._classType = value
        @property
        def lastWritten(self) -> datetime: ...
        @lastWritten.setter
        def lastWritten(self, value: datetime):
            self._lastWritten = value


    class RegistryKeyName(vmodl.DynamicData):
        @property
        def registryPath(self) -> str: ...
        @registryPath.setter
        def registryPath(self, value: str):
            self._registryPath = value
        @property
        def wowBitness(self) -> str: ...
        @wowBitness.setter
        def wowBitness(self, value: str):
            self._wowBitness = value


        class RegistryKeyWowBitness(Enum):
            WOWNative = "WOWNative"
            WOW32 = "WOW32"
            WOW64 = "WOW64"


    class RegistryKeyRecord(vmodl.DynamicData):
        @property
        def key(self) -> WindowsRegistryManager.RegistryKey: ...
        @key.setter
        def key(self, value: WindowsRegistryManager.RegistryKey):
            self._key = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


    class RegistryValue(vmodl.DynamicData):
        @property
        def name(self) -> WindowsRegistryManager.RegistryValueName: ...
        @name.setter
        def name(self, value: WindowsRegistryManager.RegistryValueName):
            self._name = value
        @property
        def data(self) -> WindowsRegistryManager.RegistryValueData: ...
        @data.setter
        def data(self, value: WindowsRegistryManager.RegistryValueData):
            self._data = value


    class RegistryValueBinary(WindowsRegistryManager.RegistryValueData):
        @property
        def value(self) -> binary: ...
        @value.setter
        def value(self, value: binary):
            self._value = value


    class RegistryValueData(vmodl.DynamicData): ...


    class RegistryValueDword(WindowsRegistryManager.RegistryValueData):
        @property
        def value(self) -> int: ...
        @value.setter
        def value(self, value: int):
            self._value = value


    class RegistryValueExpandString(WindowsRegistryManager.RegistryValueData):
        @property
        def value(self) -> str: ...
        @value.setter
        def value(self, value: str):
            self._value = value


    class RegistryValueMultiString(WindowsRegistryManager.RegistryValueData):
        @property
        def value(self) -> List[str]: ...
        @value.setter
        def value(self, value: List[str]):
            self._value = value


    class RegistryValueName(vmodl.DynamicData):
        @property
        def keyName(self) -> WindowsRegistryManager.RegistryKeyName: ...
        @keyName.setter
        def keyName(self, value: WindowsRegistryManager.RegistryKeyName):
            self._keyName = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value


    class RegistryValueQword(WindowsRegistryManager.RegistryValueData):
        @property
        def value(self) -> long: ...
        @value.setter
        def value(self, value: long):
            self._value = value


    class RegistryValueString(WindowsRegistryManager.RegistryValueData):
        @property
        def value(self) -> str: ...
        @value.setter
        def value(self, value: str):
            self._value = value


class GuestAuthentication(vmodl.DynamicData):
    @property
    def interactiveSession(self) -> bool: ...
    @interactiveSession.setter
    def interactiveSession(self, value: bool):
        self._interactiveSession = value


class NamePasswordAuthentication(GuestAuthentication):
    @property
    def username(self) -> str: ...
    @username.setter
    def username(self, value: str):
        self._username = value
    @property
    def password(self) -> str: ...
    @password.setter
    def password(self, value: str):
        self._password = value


class SAMLTokenAuthentication(GuestAuthentication):
    @property
    def token(self) -> str: ...
    @token.setter
    def token(self, value: str):
        self._token = value
    @property
    def username(self) -> str: ...
    @username.setter
    def username(self, value: str):
        self._username = value


class SSPIAuthentication(GuestAuthentication):
    @property
    def sspiToken(self) -> str: ...
    @sspiToken.setter
    def sspiToken(self, value: str):
        self._sspiToken = value


class TicketedSessionAuthentication(GuestAuthentication):
    @property
    def ticket(self) -> str: ...
    @ticket.setter
    def ticket(self, value: str):
        self._ticket = value