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
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm.guest import GuestAuthentication

class FileManager(ManagedObject):
   class FileAttributes(DynamicData):
      modificationTime: Optional[datetime] = None
      accessTime: Optional[datetime] = None
      symlinkTarget: Optional[str] = None

   class PosixFileAttributes(FileAttributes):
      ownerId: Optional[int] = None
      groupId: Optional[int] = None
      permissions: Optional[long] = None

   class WindowsFileAttributes(FileAttributes):
      hidden: Optional[bool] = None
      readOnly: Optional[bool] = None
      createTime: Optional[datetime] = None

   class FileInfo(DynamicData):
      class FileType(Enum):
         file: ClassVar['FileType'] = 'file'
         directory: ClassVar['FileType'] = 'directory'
         symlink: ClassVar['FileType'] = 'symlink'

      path: str
      type: str
      size: long
      attributes: FileAttributes

   class ListFileInfo(DynamicData):
      files: list[FileInfo] = []
      remaining: int

   class FileTransferInformation(DynamicData):
      attributes: FileAttributes
      size: long
      url: str

   def MakeDirectory(self, vm: VirtualMachine, auth: GuestAuthentication, directoryPath: str, createParentDirectories: bool) -> NoReturn: ...
   def DeleteFile(self, vm: VirtualMachine, auth: GuestAuthentication, filePath: str) -> NoReturn: ...
   def DeleteDirectory(self, vm: VirtualMachine, auth: GuestAuthentication, directoryPath: str, recursive: bool) -> NoReturn: ...
   def MoveDirectory(self, vm: VirtualMachine, auth: GuestAuthentication, srcDirectoryPath: str, dstDirectoryPath: str) -> NoReturn: ...
   def MoveFile(self, vm: VirtualMachine, auth: GuestAuthentication, srcFilePath: str, dstFilePath: str, overwrite: bool) -> NoReturn: ...
   def CreateTemporaryFile(self, vm: VirtualMachine, auth: GuestAuthentication, prefix: str, suffix: str, directoryPath: Optional[str]) -> str: ...
   def CreateTemporaryDirectory(self, vm: VirtualMachine, auth: GuestAuthentication, prefix: str, suffix: str, directoryPath: Optional[str]) -> str: ...
   def ListFiles(self, vm: VirtualMachine, auth: GuestAuthentication, filePath: str, index: Optional[int], maxResults: Optional[int], matchPattern: Optional[str]) -> ListFileInfo: ...
   def ChangeFileAttributes(self, vm: VirtualMachine, auth: GuestAuthentication, guestFilePath: str, fileAttributes: FileAttributes) -> NoReturn: ...
   def InitiateFileTransferFromGuest(self, vm: VirtualMachine, auth: GuestAuthentication, guestFilePath: str) -> FileTransferInformation: ...
   def InitiateFileTransferToGuest(self, vm: VirtualMachine, auth: GuestAuthentication, guestFilePath: str, fileAttributes: FileAttributes, fileSize: long, overwrite: bool) -> str: ...
