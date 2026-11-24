# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl



class AliasManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   The GuestAliasManager supports single sign-on for virtual machine access
   to perform guest operations.
   
   The GuestAliasManager provides methods
   to create and access aliases.
   
   A guest alias defines an association between a guest user account on a virtual
   machine
   and an external vSphere user account. The vSphere account is represented by
   credentials consisting of an X.509 certificate and a subject name.
   The certificate and subject name
   are encoded
   in SAML tokens that are provided by the VMware SSO Server. The SAML tokens
   are attached
   to guest operation requests. If the credentials in a SAML token match an
   alias that is defined
   for a virtual machine, the ESXi Server guest components grant
   access for execution of the
   guest operation
   in the context of the user account on the virtual machine.
   
   To create a guest alias, use the AddGuestAlias method. AddGuestAlias
   establishes
   the association between a guest user account, certificate, and SAML token subject.
   - The username parameter identifies the guest account.
   - The base64Cert parameter specifies the X.509 certificate.
   - The aliasInfo parameter identifies the SAML token subject
     (`pyVmomi.vim.vm.guest.AliasManager.GuestAuthAliasInfo`.
     `pyVmomi.vim.vm.guest.AliasManager.GuestAuthAliasInfo.subject`.
     `pyVmomi.vim.vm.guest.AliasManager.GuestAuthNamedSubject.name`).
     
   If there are no aliases defined for a virtual machine, the ESXi Server
   will perform
   standard authentication using the credentials associated with a guest
   operation request.
   If one or more aliases are defined for a virtual machine, any guest
   operation request
   that uses SAML token authentication SAMLTokenAuthentication must specify
   a token
   that corresponds to one of the defined aliases.
   
   After defining one or more guest aliases, you can specify
   `pyVmomi.vim.vm.guest.SAMLTokenAuthentication` for the
   auth parameter to guest operation methods:
   - `pyVmomi.vim.vm.guest.ProcessManager` methods
   - `pyVmomi.vim.vm.guest.FileManager` methods
   - `pyVmomi.vim.vm.guest.WindowsRegistryManager` methods
     
   For information about obtaining a SAML token from a VMware SSO Server,
   see VMware Single Sign-On Programming Guide.
   
   You can define multiple aliases for a guest account. You can also
   map the credentials
   to an alias by setting mapCert to \"true\" in the call to the
   AddGuestAlias method.
   When an alias has a mapped credential, requests using that alias do not
   need to identify the guest account.
   """
   class GuestAuthSubject(pyVmomi.vmodl.DynamicData):
      """A Subject."""
      pass

   class GuestAuthAnySubject(AliasManager.GuestAuthSubject):
      """
      The ANY subject.
      
      When an in-guest user account is configured
      to trust an alias using the ANY subject, any vSphere user
      authenticated by that alias will be allowed to impersonate the
      in-guest user.
      """
      pass

   class GuestAuthNamedSubject(AliasManager.GuestAuthSubject):
      """
      A named subject.
      
      Grants access to a specific vSphere user with
      the specified name.
      
      Attributes:
          name: The subject name.
      """
      name: str

   class GuestAuthAliasInfo(pyVmomi.vmodl.DynamicData):
      """
      Describes a subject associated with an X.509 certificate in the alias
      store.
      
      Attributes:
          subject: The subject.
          comment: User-supplied data to describe the subject.
      """
      subject: AliasManager.GuestAuthSubject
      comment: str

   class GuestAliases(pyVmomi.vmodl.DynamicData):
      """
      Describes the representation of an alias and the subjects
      that are trusted from that VMware SSO Server.
      
      Attributes:
          base64Cert: The associated VMware SSO Server X.509 certificate, in base64
              encoded DER format.
          aliases: A white list of aliases that the in-guest user account trusts;
              it can be a subset of the subjects known to the identity
              provider.
      """
      base64Cert: str
      aliases: list[AliasManager.GuestAuthAliasInfo] = []

   class GuestMappedAliases(pyVmomi.vmodl.DynamicData):
      """
      Represents a mapping between an external subject, as
      authenticated by a given VMware SSO Server, and an in-guest user.
      
      Attributes:
          base64Cert: The associated VMware SSO Server X.509 certificate, in base64
              encoded DER format.
          username: The in-guest user associated with the mapping.
          subjects: The list of subjects associated with the mapping.
      """
      base64Cert: str
      username: str
      subjects: list[AliasManager.GuestAuthSubject] = []

   def AddAlias(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, username: str, mapCert: bool, base64Cert: str, aliasInfo: AliasManager.GuestAuthAliasInfo) -> None:
      """
      Defines an alias for a guest account in a virtual machine.
      
      After the alias is defined, the ESXi Server will use the alias
      to authenticate guest operations requests.
      
      This will add the given VMware SSO Server's certificate and a
      subject to the alias store of the
      specified user in the guest.
      
      In order to add an alias to the guest, you must supply
      an existing valid credential. This can be any instance
      of `pyVmomi.vim.vm.guest.GuestAuthentication`, but must be valid for the
      specified guest username.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data for this operation. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`. These credentials must satisfy
              authentication requirements
              for a guest account on the specified virtual machine.
          username: Username for the guest account on the virtual machine.
          mapCert: Indicates whether the certificate associated with the
              alias should be mapped. If an alias certificate is mapped,
              guest operation requests that use that alias do not have
              to specify the guest account username in the
              `pyVmomi.vim.vm.guest.SAMLTokenAuthentication` object. If mapCert is
              false, the request must specify the username.
          base64Cert: X.509 certificate from the VMware SSO Server,
              in base64 encoded DER format. The ESXi
              Server uses this certificate to authenticate guest
              operation requests.
          aliasInfo: Specifies the subject name for authentication.
              The subject name (when present) corresponds to
              the value of the Subject element
              in SAML tokens. The ESXi Server uses the subject
              name to authenticate guest operation requests.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def RemoveAlias(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, username: str, base64Cert: str, subject: AliasManager.GuestAuthSubject) -> None:
      """
      Removes an alias from the guest so it can no longer be
      used for
      authentication of guest operations.
      
      It will also be removed
      from the mapped credentials.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data for this operation. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`. These credentials must satisfy
              authentication requirements
              for a guest account on the specified virtual machine.
          username: Username for the guest account on the virtual machine.
          base64Cert: The X.509 certificate associated with the alias to be
              removed, in base64 encoded DER format.
          subject: The subject of the alias.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def RemoveAliasByCert(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, username: str, base64Cert: str) -> None:
      """
      Removes a VMware SSO Server's certificate and all
      associated aliases from the guest so it
      can no longer be used for
      authentication of guest operations.
      
      It will also be removed
      from the global certificate-to-user mapping file in the guest.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data for this operation. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`. These credentials must satisfy
              authentication requirements
              for a guest account on the specified virtual machine.
          username: Username for the guest account on the virtual machine.
          base64Cert: The X.509 certificate to be removed, in base64
              encoded DER format.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def ListAliases(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, username: str) -> list[AliasManager.GuestAliases]:
      """
      Lists the
      `pyVmomi.vim.vm.guest.AliasManager.GuestAliases`
      for a specified user in the guest that can be used
      for authentication of guest operations.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data for this operation. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`. These credentials must satisfy
              authentication requirements
              for a guest account on the specified virtual machine.
          username: The guest user whose Alias store is being queried.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def ListMappedAliases(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication) -> list[AliasManager.GuestMappedAliases]:
      """
      Lists the
      `pyVmomi.vim.vm.guest.AliasManager.GuestMappedAliases`
      in the guest that can be used for
      authentication of guest operations.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data for this operation. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`. These credentials must satisfy
              authentication requirements
              for a guest account on the specified virtual machine.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...


class AuthManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   AuthManager is the managed object that provides APIs
   to manipulate the guest operating authentication.
   """
   def ValidateCredentials(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication) -> None:
      """
      Validates the `pyVmomi.vim.vm.guest.GuestAuthentication` credentials.
      
      This can be used to check the authentication data, or
      validate any authentication that has a timeout is still valid.
      If the authentication is not valid, `pyVmomi.vim.fault.GuestPermissionDenied`
      will be thrown.
      
      Args:
          vm: MoRef of the VM to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def AcquireCredentials(self, vm: pyVmomi.vim.VirtualMachine, requestedAuth: GuestAuthentication, sessionID: _typing.Optional[pyVmomi.VmomiSupport.long]) -> GuestAuthentication:
      """
      Authenticates in the guest and returns a `pyVmomi.vim.vm.guest.GuestAuthentication` object
      with the acquired credentials for use in subsequent guest operation calls.
      
      This can be used to authenticate inside the guest and obtain a
      `pyVmomi.vim.vm.guest.GuestAuthentication` object for supported authentication types.
      This operation is not needed for Name and Password Authentication. To use
      Name and Password Authentication, see `pyVmomi.vim.vm.guest.NamePasswordAuthentication`.
      For SSPI authentication, requestAuth should be of the type `pyVmomi.vim.vm.guest.SSPIAuthentication`.
      
      Args:
          vm: MoRef of the VM to perform the operation on.
          requestedAuth: The guest authentication data used to acquire credentials.
              See `pyVmomi.vim.vm.guest.GuestAuthentication`.
          sessionID: The sessionID number should be provided only when
              responding to a server challenge. The sessionID number to be used with
              the challenge is found in the
              `pyVmomi.vim.fault.GuestAuthenticationChallenge` object.
      
      Returns:
          Returns a `pyVmomi.vim.vm.guest.GuestAuthentication` object that can be used in
          guest operation calls.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
      """
      ...
   def ReleaseCredentials(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication) -> None:
      """
      Releases session data and resources associated with
      a `pyVmomi.vim.vm.guest.GuestAuthentication` object returned by `pyVmomi.vim.vm.guest.AuthManager.acquireCredentials`.
      
      This frees any resources and session data associated with a
      `pyVmomi.vim.vm.guest.GuestAuthentication` object returned by `pyVmomi.vim.vm.guest.AuthManager.acquireCredentials`.
      The `pyVmomi.vim.vm.guest.GuestAuthentication` object can no longer be used to
      authenticate in the guest once released. Currently this operation is only
      valid for `pyVmomi.vim.vm.guest.TicketedSessionAuthentication` objects.
      
      Args:
          vm: MoRef of the VM to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
      """
      ...


class FileManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   FileManager is the managed object that provides APIs
   to manipulate the guest operating system files.
   """
   class FileAttributes(pyVmomi.vmodl.DynamicData):
      """
      Different attributes for a guest file.
      - Check `pyVmomi.vim.vm.guest.FileManager.PosixFileAttributes`
        for Posix guest files.
      - Check `pyVmomi.vim.vm.guest.FileManager.WindowsFileAttributes`
        for Windows guest files.
      
      Attributes:
          modificationTime: The date and time the file was last modified.
              
              If this property is not specified when passing a
              `pyVmomi.vim.vm.guest.FileManager.FileAttributes` object to
              `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferToGuest`,
              the default value will be the time when the file is created inside the
              guest.
          accessTime: The date and time the file was last accessed.
              
              If this property is not specified when passing a
              `pyVmomi.vim.vm.guest.FileManager.FileAttributes` object to
              `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferToGuest`,
              the default value will be the time when the file is created inside the
              guest.
          symlinkTarget: The target for the file if it's a symbolic link.
              
              This is currently only set for Linux guest operating systems,
              but may be supported in the
              future on Windows guest operating systems that support symbolic links.
              This property gives information about files when returned from
              `pyVmomi.vim.vm.guest.FileManager.listFiles` or
              `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferFromGuest`
              as part of a `pyVmomi.vim.vm.guest.FileManager.FileAttributes` object.
              This property will be ignored when passing a
              `pyVmomi.vim.vm.guest.FileManager.FileAttributes` object to
              `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferToGuest` or
              `pyVmomi.vim.vm.guest.FileManager.changeFileAttributes`.
              If the file is a symbolic link, then the attributes of the target
              are returned, not those of the symbolic link.
      """
      modificationTime: _typing.Optional[_datetime.datetime] = None
      accessTime: _typing.Optional[_datetime.datetime] = None
      symlinkTarget: _typing.Optional[str] = None

   class PosixFileAttributes(FileManager.FileAttributes):
      """
      Different attributes for Posix guest file.
      
      Attributes:
          ownerId: The owner ID.
              
              If this property is not specified when passing a
              `pyVmomi.vim.vm.guest.FileManager.PosixFileAttributes` object to
              `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferToGuest`,
              the default value will be the owner Id of the user who invoked
              the file transfer operation.
          groupId: The group ID.
              
              If this property is not specified when passing a
              `pyVmomi.vim.vm.guest.FileManager.PosixFileAttributes` object to
              `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferToGuest`,
              the default value will be the group Id of the user who invoked
              the file transfer operation.
          permissions: The file permissions.
              
              When creating a file with
              `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferToGuest`,
              these are in chmod(2) format. When reporting on
              existing files, these are in stat(2) format.
              If this property is not specified when passing a
              `pyVmomi.vim.vm.guest.FileManager.PosixFileAttributes` object to
              `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferToGuest`,
              the file will be created with 0644 permissions.
      """
      ownerId: _typing.Optional[int] = None
      groupId: _typing.Optional[int] = None
      permissions: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class WindowsFileAttributes(FileManager.FileAttributes):
      """
      Different attributes for a Windows guest file.
      
      Attributes:
          hidden: The file is hidden.
              
              If this property is not specified when passing a
              `pyVmomi.vim.vm.guest.FileManager.WindowsFileAttributes` object to
              `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferToGuest`,
              the file will not be set as a hidden file.
          readOnly: The file is read-only.
              
              If this property is not specified when passing a
              `pyVmomi.vim.vm.guest.FileManager.WindowsFileAttributes` object to
              `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferToGuest`,
              the file will not be set as a read-only file.
          createTime: The date and time the file was created.
              
              This property gives information about files when returned from
              `pyVmomi.vim.vm.guest.FileManager.listFiles` or
              `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferFromGuest`
              as part of a `pyVmomi.vim.vm.guest.FileManager.WindowsFileAttributes`
              object. This property will be ignored when passing a
              `pyVmomi.vim.vm.guest.FileManager.WindowsFileAttributes` object to
              `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferToGuest` or
              `pyVmomi.vim.vm.guest.FileManager.changeFileAttributes`.
      """
      hidden: _typing.Optional[bool] = None
      readOnly: _typing.Optional[bool] = None
      createTime: _typing.Optional[_datetime.datetime] = None

   class FileInfo(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          path: The complete path to the file
          type: The file type, one of `pyVmomi.vim.vm.guest.FileManager.FileInfo.FileType`
          size: The file size in bytes
          attributes: Different attributes of a file.
      """
      class FileType(pyVmomi.VmomiSupport.Enum):
         """
         Attributes:
             file: Regular files, and on Posix filesystems, unix domain sockets
                 and devices.
             directory: directory
             symlink: symbolic link
         """
         file: _typing.ClassVar['FileManager.FileInfo.FileType'] = 'file'
         directory: _typing.ClassVar['FileManager.FileInfo.FileType'] = 'directory'
         symlink: _typing.ClassVar['FileManager.FileInfo.FileType'] = 'symlink'

      path: str
      type: str
      size: pyVmomi.VmomiSupport.long
      attributes: FileManager.FileAttributes

   class ListFileInfo(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          files: A list of `pyVmomi.vim.vm.guest.FileManager.FileInfo`
              data objects containing information for all the matching files.
          remaining: The number of files left to be returned.
              
              If non-zero,
              then the next set of files can be returned by calling
              ListFiles again with the index set to the number of results
              already returned.
      """
      files: list[FileManager.FileInfo] = []
      remaining: int

   class FileTransferInformation(pyVmomi.vmodl.DynamicData):
      """
      Represents the information about a
      `pyVmomi.vim.vm.guest.FileManager.initiateFileTransferFromGuest` operation
      of `pyVmomi.vim.vm.guest.FileManager` object.
      
      The user can use the URL provided in url property to transfer
      the file from the guest. The user should send a HTTP GET request to the
      URL. Entire file content will be returned in the body of the response
      message.
      
      Attributes:
          attributes: File attributes of the file that is being transferred from the guest.
          size: Total size of the file in bytes.
          url: Specifies the URL to which the user has to send HTTP GET request.
              
              Multiple GET requests cannot be sent to the URL simultaneously. URL
              will become invalid once a successful GET request is sent.
                
                
              The host part of the URL is returned as '*' if the hostname to be used
              is the name of the server to which the call was made. For example, if
              the call is made to esx-svr-1.domain1.com, and the file is available for
              download from
              `https://esx-svr-1.domain1.com/guestFile?id=1&token=1234`,
              the URL returned may be
              `https://*/guestFile?id=1&token=1234`.
              The client replaces the asterisk with the server name on which it
              invoked the call.
                
                
              The URL is valid only for 10 minutes from the time it is generated.
              Also, the URL becomes invalid whenever the virtual machine is powered
              off, suspended or unregistered.
      """
      attributes: FileManager.FileAttributes
      size: pyVmomi.VmomiSupport.long
      url: str

   def MakeDirectory(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, directoryPath: str, createParentDirectories: bool) -> None:
      """
      Creates a directory in the guest OS
      
      Args:
          vm: Virtual Machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          directoryPath: The complete path to the directory to be created.
          createParentDirectories: Whether any parent directories
              are to be created.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.FileFault: if there is a file error in the guest operating system.
      """
      ...
   def DeleteFile(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, filePath: str) -> None:
      """
      Deletes a file in the guest OS
      
      Args:
          vm: Virtual Machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          filePath: The complete path to the file or symbolic link to be deleted.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.FileFault: if there is a file error in the guest operating system.
      """
      ...
   def DeleteDirectory(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, directoryPath: str, recursive: bool) -> None:
      """
      Deletes a directory in the guest OS.
      
      Args:
          vm: Virtual Machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          directoryPath: The complete path to the directory to be deleted.
          recursive: If true, all subdirectories are also deleted.
              If false, the directory must be empty for the operation to succeed.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.FileFault: if there is a file error in the guest operating system.
      """
      ...
   def MoveDirectory(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, srcDirectoryPath: str, dstDirectoryPath: str) -> None:
      """
      Moves or renames a directory in the guest.
      
      Args:
          vm: Virtual Machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          srcDirectoryPath: The complete path to the directory to be moved.
          dstDirectoryPath: The complete path to the where the directory is
              moved or its new name. It cannot be a path to an existing directory
              or an existing file.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.FileFault: if there is a file error in the guest operating system.
      """
      ...
   def MoveFile(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, srcFilePath: str, dstFilePath: str, overwrite: bool) -> None:
      """
      Renames a file in the guest.
      
      Args:
          vm: Virtual Machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          srcFilePath: The complete path to the original file or
              symbolic link to be moved.
          dstFilePath: The complete path to the where the file is renamed.
              It cannot be a path to an existing directory.
          overwrite: If set, the destination file is clobbered.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.FileFault: if there is a file error in the guest operating system.
      """
      ...
   def CreateTemporaryFile(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, prefix: str, suffix: str, directoryPath: _typing.Optional[str]) -> str:
      """
      Creates a temporary file.
      
      Creates a new unique temporary file for the user to use as needed.
      The user is responsible for removing it when it is no longer needed.
      
      Args:
          vm: Virtual Machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          prefix: The prefix to be given to the new temporary file.
          suffix: The suffix to be given to the new temporary file.
          directoryPath: The complete path to the directory in which to
              create the file.
              If unset, or an empty string, a guest-specific location will be used.
      
      Returns:
          The absolute path of the temporary file that is created.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.FileFault: if there is a file error in the guest operating system.
      """
      ...
   def CreateTemporaryDirectory(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, prefix: str, suffix: str, directoryPath: _typing.Optional[str]) -> str:
      """
      Creates a temporary directory.
      
      Creates a new unique temporary directory for the user to use as needed.
      The user is responsible for removing it when it is no longer needed.
      
      Args:
          vm: Virtual Machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          prefix: The prefix to be given to the new temporary directory.
          suffix: The suffix to be given to the new temporary directory.
          directoryPath: The complete path to the directory in which to create the
              new directory. If unset or an empty string, a guest-specific location
              will be used.
      
      Returns:
          The absolute path of the temporary directory that is created.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.FileFault: if there is a file error in the guest operating system.
      """
      ...
   def ListFiles(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, filePath: str, index: _typing.Optional[int], maxResults: _typing.Optional[int], matchPattern: _typing.Optional[str]) -> FileManager.ListFileInfo:
      """
      Returns information about files or directories in the guest.
      
      The results could be extremely large, so to minimize the size
      of the return value for cases where a UI only needs to show
      the first N results, the answer is batched. Files are returned in
      OS-specific (inode) order. If the directory is modified between
      queries, missing or duplicate results can occur.
      
      Args:
          vm: Virtual Machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          filePath: The complete path to the directory or file to query.
          index: Which result to start the list with. The default is 0.
          maxResults: The maximum number of results to return. The default
              is 50.
          matchPattern: A filter for the return values.
              Match patterns are specified using perl-compatible regular
              expressions.
              If matchPattern is unset, then the pattern '.*' is used.
      
      Returns:
          A `pyVmomi.vim.vm.guest.FileManager.ListFileInfo`
          object containing information for all the matching files
          in the filePath and the number of files left to be returned.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.FileFault: The common base type for all file-related exceptions.
      """
      ...
   def ChangeFileAttributes(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, guestFilePath: str, fileAttributes: FileManager.FileAttributes) -> None:
      """
      Changes the file attributes of a specified file inside the guest.
      
      Args:
          vm: Virtual Machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          guestFilePath: The complete path to the file to be copied in
              the guest. If the file points to an symbolic link, then the
              attributes of the target file are changed.
          fileAttributes: Specifies the different file attributes of the
              guest file to be changed.
              See `pyVmomi.vim.vm.guest.FileManager.FileAttributes`.
              If any property is not specified, then the specific attribute of
              the file will be unchanged.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.FileFault: if there is a file error in the guest operating system.
      """
      ...
   def InitiateFileTransferFromGuest(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, guestFilePath: str) -> FileManager.FileTransferInformation:
      """
      Initiates an operation to transfer a file from the guest.
      
      Obtains a reference to
      `pyVmomi.vim.vm.guest.FileManager.FileTransferInformation` object
      for the file transfer operation. The information object contains a URL
      to the file inside the guest to be transferred to the client.
        
      See `pyVmomi.vim.vm.guest.FileManager.FileTransferInformation` for
      information on how to use the information object. If the power state
      of the Virtual Machine is changed when the file transfer is in progress,
      or the Virtual Machine is migrated,
      then the transfer operation is aborted.
      
      In order to ensure a secure connection to the host when transferring
      a file using HTTPS, the X.509 certificate for the host must be used
      to authenticate the remote end of the connection. The certificate of
      the host that the virtual machine is running on can be retrieved using
      the following fields:
      vm (`pyVmomi.vim.VirtualMachine`) -> runtime (`pyVmomi.vim.vm.RuntimeInfo`)
      \\-> host (`pyVmomi.vim.HostSystem`) -> config (`pyVmomi.vim.host.ConfigInfo`)
      \\-> certificate.
      
      Args:
          vm: Virtual Machine to perform the operation on.
          auth: The guest authentication data.
          guestFilePath: The complete path to the file inside the guest
              that has to be transferred to the client. It cannot be a path to
              a directory or a symbolic link.
      
      Returns:
          A reference to
          `pyVmomi.vim.vm.guest.FileManager.FileTransferInformation`.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.FileFault: if there is a file error in the guest operating system.
      """
      ...
   def InitiateFileTransferToGuest(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, guestFilePath: str, fileAttributes: FileManager.FileAttributes, fileSize: pyVmomi.VmomiSupport.long, overwrite: bool) -> str:
      """
      Initiates an operation to transfer a file to the guest.
      
      Obtains a URL to the file inside the guest to be transferred from the
      client. The user should send a HTTP PUT request specifying the file
      content in the body of the request. Multiple PUT request cannot be
      sent to the URL simultaneously. URL will be invalidated after a
      successful PUT request is sent. If the power state of the Virtual
      Machine is changed when the file transfer is in progress, or
      the Virtual Machine is migrated, then the
      transfer operation is aborted.
      
      In order to ensure a secure connection to the host when transferring
      a file using HTTPS, the X.509 certificate for the host must be used
      to authenticate the remote end of the connection. The certificate of
      the host that the virtual machine is running on can be retrieved using
      the following fields:
      vm (`pyVmomi.vim.VirtualMachine`) -> runtime (`pyVmomi.vim.vm.RuntimeInfo`)
      \\-> host (`pyVmomi.vim.HostSystem`) -> config (`pyVmomi.vim.host.ConfigInfo`)
      \\-> certificate.
      
      Args:
          vm: Virtual Machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          guestFilePath: The complete destination path in the guest to
              transfer the file from the client. It cannot be a path to
              a directory or a symbolic link.
          fileAttributes: File attributes of the file that has to be
              created in the guest. See `pyVmomi.vim.vm.guest.FileManager.FileAttributes`.
              If any file attribute is not specified, then the default value
              of that property will be set for the file.
          fileSize: Size of the file to transfer to the guest in bytes.
          overwrite: If set, the destination file is clobbered.
      
      Returns:
          A URL to which the user has to send a PUT request.
          The host part of the URL is returned as '*' if the hostname to be
          used is the name of the server to which the call was made. For
          example, if the call is made to esx-svr-1.domain1.com, and the file
          can be uploaded to
          `https://esx-svr-1.domain1.com/guestFile?id=1&token=1234`,
          the URL returned may be
          `https://*/guestFile?id=1&token=1234`.
          The client replaces the asterisk with the server name on which it
          invoked the call.
            
            
          The URL is valid only for 10 minutes from the time it is generated.
          Also, the URL becomes invalid whenever the virtual machine is powered
          off, suspended or unregistered.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.FileFault: if there is a file error in the guest operating system.
      """
      ...


class GuestAuthentication(pyVmomi.vmodl.DynamicData):
   """
   GuestAuthentication is an abstract base class for authentication
   in the guest.
   
   Attributes:
       interactiveSession: This is set to true if the client wants an interactive session
           in the guest.
           
           Setting this is supported only for `pyVmomi.vim.vm.guest.NamePasswordAuthentication`.
   """
   interactiveSession: bool


class GuestOperationsManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   GuestOperationsManager is the managed object that provides APIs
   to manipulate the guest operating system files and process.
   
   Each class of APIs is separated into its own manager.
   Only one guest operation is allowed at a time per virtual machine.
   """
   @property
   def authManager(self) -> _typing.Optional[AuthManager]:
      """
      A singleton managed object that provides methods for guest authentication
      operations.
      """
      ...
   @property
   def fileManager(self) -> _typing.Optional[FileManager]:
      """
      A singleton managed object that provides methods for guest file
      operations.
      """
      ...
   @property
   def processManager(self) -> _typing.Optional[ProcessManager]:
      """
      A singleton managed object that provides methods for guest process
      operations.
      """
      ...
   @property
   def guestWindowsRegistryManager(self) -> _typing.Optional[WindowsRegistryManager]:
      """
      A singleton managed object that provides methods for guest windows registry
      operations.
      """
      ...
   @property
   def aliasManager(self) -> _typing.Optional[AliasManager]:
      """
      A managed object that provides methods to support single sign-on
      in the guest operating system.
      """
      ...

class NamePasswordAuthentication(GuestAuthentication):
   """
   NamePasswordAuthentication contains the information necessary to authenticate
   within a guest using a name and password.
   
   This is the typical method for
   authentication within a guest and the one currently used by VIX.
   This method of authentication is stateless.
   
   To use NamePasswordAuthentication, populate username and password with the
   appropriate login information. You should not use `pyVmomi.vim.vm.guest.AuthManager.acquireCredentials`
   or `pyVmomi.vim.vm.guest.AuthManager.releaseCredentials` for NamePasswordAuthentication.
   
   Once populated, you can use NamePasswordAuthentication in any guest operations function call.
   
   Attributes:
       username: The user name for Name-Password authentication.
       password: The password for Name-Password authentication.
   """
   username: str
   password: str


class ProcessManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   ProcessManager is the managed object that provides APIs
   to manipulate the guest operating system processes.
   """
   class ProgramSpec(pyVmomi.vmodl.DynamicData):
      """
      This describes the arguments to `pyVmomi.vim.vm.guest.ProcessManager.startProgram`.
      
      Attributes:
          programPath: The absolute path to the program to start.
              
              For Linux guest operating systems, /bin/bash is used to start the
              program.
              
              For Solaris guest operating systems, /bin/bash is used to start
              the program if it exists.
              Otherwise /bin/sh is used. If /bin/sh is used, then the process ID
              returned by `pyVmomi.vim.vm.guest.ProcessManager.startProgram` will be that of the shell used
              to start the program, rather than the program itself, due to the
              differences in how /bin/sh and /bin/bash work. This PID will
              still be usable for watching the process with
              `pyVmomi.vim.vm.guest.ProcessManager.listProcesses` to
              find its exit code and elapsed time.
          arguments: The arguments to the program.
              
              In Linux and Solaris guest operating
              systems, the program will be executed by a guest shell.
              This allows stdio redirection, but may also
              require that characters which must be escaped to the shell also
              be escaped on the command line provided.
              
              For Windows guest operating systems, prefixing the command with
              \"cmd /c\" can provide stdio redirection.
          workingDirectory: The absolute path of the working directory for the program to be
              run.
              
              VMware recommends explicitly setting the working directory
              for the program to be run. If this value is unset or is an empty
              string, the behavior depends on the guest operating system.
              For Linux guest operating systems, if this value is unset or is
              an empty string, the working directory will be the home directory
              of the user associated with the guest authentication.
              For other guest operating systems, if this value is unset, the
              behavior is unspecified.
          envVariables: An array of environment variables, specified
              in the guest OS notation (eg PATH=c:\\bin;c:\\windows\\system32
              or LD_LIBRARY_PATH=/usr/lib:/lib), to be set for the program
              being run.
              
              Note that these are not additions to the default
              environment variables; they define the complete set available to
              the program. If none are specified the values are guest dependent.
      """
      programPath: str
      arguments: str
      workingDirectory: _typing.Optional[str] = None
      envVariables: list[str] = []

   class WindowsProgramSpec(ProcessManager.ProgramSpec):
      """
      This describes the arguments to `pyVmomi.vim.vm.guest.ProcessManager.startProgram` that apply
      only for Windows guests.
      
      Attributes:
          startMinimized: Makes any program window start minimized.
      """
      startMinimized: bool

   class ProcessInfo(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          name: The process name
          pid: The process ID
          owner: The process owner
          cmdLine: The full command line
          startTime: The start time of the process
          endTime: If the process was started using
              `pyVmomi.vim.vm.guest.ProcessManager.startProgram`
              then the process completion time will be available if
              queried within 5 minutes after it completes.
          exitCode: If the process was started using
              `pyVmomi.vim.vm.guest.ProcessManager.startProgram`
              then the process exit code will be available if
              queried within 5 minutes after it completes.
      """
      name: str
      pid: pyVmomi.VmomiSupport.long
      owner: str
      cmdLine: str
      startTime: _datetime.datetime
      endTime: _typing.Optional[_datetime.datetime] = None
      exitCode: _typing.Optional[int] = None

   def StartProgram(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, spec: ProcessManager.ProgramSpec) -> pyVmomi.VmomiSupport.long:
      """
      Starts a program in the guest operating system.
      
      A process started this way can have its status queried with
      `pyVmomi.vim.vm.guest.ProcessManager.listProcesses`.
      When the process completes, its exit code and end time will be
      available for 5 minutes after completion.
      
      If VMware Tools is restarted, the exit code and end time will not
      be available.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          spec: The arguments describing the program to be started.
      
      Returns:
          The pid of the program started.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.FileFault: if there is a file error in the guest operating system.
      """
      ...
   def ListProcesses(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, pids: list[pyVmomi.VmomiSupport.long]) -> list[ProcessManager.ProcessInfo]:
      """
      List the processes running in the guest operating system,
      plus those started by `pyVmomi.vim.vm.guest.ProcessManager.startProgram`
      that have recently completed.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          pids: If set, only return information about the specified processes.
              Otherwise, information about all processes are returned.
              If a specified processes does not exist, nothing will
              be returned for that process.
      
      Returns:
          The list running processes is returned in an array of
          `pyVmomi.vim.vm.guest.ProcessManager.ProcessInfo` structures.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def TerminateProcess(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, pid: pyVmomi.VmomiSupport.long) -> None:
      """
      Terminates a process in the guest OS.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          pid: Process ID of the process to be terminated
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def ReadEnvironmentVariable(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, names: list[str]) -> list[str]:
      """
      Reads an environment variable from the guest OS
      
      If the authentication uses interactiveSession, then the
      environment being read will be that of the user logged into the desktop.
      Otherwise it's the environment of the user specified by the auth.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          names: The names of the variables to be read. If not set, then
              all the environment variables are returned.
      
      Returns:
          A string array containing the value of the variables,
          or all environment variables if nothing is specified.
          The format of each string is \"name=value\".
          If any specified environment variable isn't set, then nothing is
          returned for that variable.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
              accepted by the guest OS.
      """
      ...


class SAMLTokenAuthentication(GuestAuthentication):
   """
   SAMLTokenAuthentication contains the information necessary to authenticate
   within a guest using a SAML bearer token.
   
   SAML token authentication relies on a guest alias that associates a guest
   account with the subject and certificate
   encoded in a SAML token obtained from the VMware SSO Server.
   - Use the `pyVmomi.vim.vm.guest.AliasManager`.
     `pyVmomi.vim.vm.guest.AliasManager.addAlias` method to create a guest
     alias.
   - Use a SAMLTokenAuthentication object for the
     auth parameter to guest operations methods.
     
   After you have created an alias, you can use SAML token authentication
   for guest operations methods.
   Do not use SAML token authentication for the
   `pyVmomi.vim.vm.guest.AuthManager.acquireCredentials` and
   `pyVmomi.vim.vm.guest.AuthManager.releaseCredentials` methods.
   
   Attributes:
       token: The SAML bearer token.
       username: This is the guest user to be associated with the authentication.
           
           If none is specified, a guest dependent mapping will decide what
           user account is applied.
   """
   token: str
   username: _typing.Optional[str] = None

class SSPIAuthentication(GuestAuthentication):
   """
   SSPIAuthentication contains the information necessary to
   initiate a ticketed authentication session in the guest
   using SSPI credentials.
   
   The ticketed session is not stateless and stores state inside of the guest.
   
   To use SSPIAuthentication, populate sspiToken with a base64 encoded SSPI token.
   Then call `pyVmomi.vim.vm.guest.AuthManager.acquireCredentials` with
   the SSPIAuthentication object and no sessionID.
   After issuing the `pyVmomi.vim.vm.guest.AuthManager.acquireCredentials` call, a
   `pyVmomi.vim.fault.GuestAuthenticationChallenge` will be thrown.
   Use the serverChallenge sspiToken in `pyVmomi.vim.fault.GuestAuthenticationChallenge`
   to generate the proper SSPI response token.
   Populate an SSPIAuthentication object with the base64 encoded SSPI response token, and
   call `pyVmomi.vim.vm.guest.AuthManager.acquireCredentials` with the SSPIAuthentication object and
   the sessionID found in `pyVmomi.vim.fault.GuestAuthenticationChallenge`.
   
   Successful authentication will result in a `pyVmomi.vim.vm.guest.TicketedSessionAuthentication`
   object being returned. You can use the `pyVmomi.vim.vm.guest.TicketedSessionAuthentication` in any
   guest operations function call. You should NOT attempt to use SSPIAuthentication in any guest
   operations function call.
   
   When you no longer need the `pyVmomi.vim.vm.guest.TicketedSessionAuthentication` object, you should
   call `pyVmomi.vim.vm.guest.AuthManager.releaseCredentials` to free associated resources
   and session data.
   
   Usage notes: SSPI authentication has the same limitations as a duplicated primary token obtained
   from the Windows API function LogonUser with the LOGON32_LOGON_NETWORK logon type. This will affect
   programs started with `pyVmomi.vim.vm.guest.ProcessManager.startProgram`. For example, launched
   programs will be unable to use WMI functions unless the \"Remote Enable\" privilege is enabled for
   the user. Similarly, access to network resources may fail due to the limitations of the token.
   
   Attributes:
       sspiToken: This contains a base64 encoded SSPI Token.
   """
   sspiToken: str

class TicketedSessionAuthentication(GuestAuthentication):
   """
   TicketedSessionAuthentication contains the information necessary to
   use previously obtained credentials in the guest.
   
   The ticketed session is not stateless and stores state inside of the guest.
   
   A TicketedSessionAuthentication object will be returned as the result of a
   successful call to `pyVmomi.vim.vm.guest.AuthManager.acquireCredentials`. You can
   use this object in any guest operations function call.
   
   When you no longer need the TicketedSessionAuthentication object, you should
   call `pyVmomi.vim.vm.guest.AuthManager.releaseCredentials` to free associated resources
   and session data.
   
   Attributes:
       ticket: This contains a base64 encoded Ticket.
   """
   ticket: str


class WindowsRegistryManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   WindowsRegistryManager is the managed object that provides APIs
   to manipulate the Registry in a Windows guest OS.
   """
   class RegistryKeyName(pyVmomi.vmodl.DynamicData):
      """
      This describes the registry key name.
      
      Attributes:
          registryPath: The full path to a registry key.
          wowBitness: The wow bitness, one of `pyVmomi.vim.vm.guest.WindowsRegistryManager.RegistryKeyName.RegistryKeyWowBitness`.
      """
      class RegistryKeyWowBitness(pyVmomi.VmomiSupport.Enum):
         """
         This describes the bitness (32-bit or 64-bit) of a registry view in a
         Windows OS that supports WOW64.
         
         WOW64 (short for Windows 32-bit on Windows 64-bit) is the x86 emulator
         that allows 32-bit Windows-based applications to run seamlessly on
         64-bit Windows. Please refer to these MSDN sites for more details:
         http://msdn.microsoft.com/en-us/library/aa384249(v=vs.85).aspx and
         http://msdn.microsoft.com/en-us/library/aa384253(v=vs.85).aspx
         
         Attributes:
             WOWNative: Access the key from the native view of the
                 Registry (32-bit on 32-bit versions of Windows,
                 64-bit on 64-bit versions of Windows).
             WOW32: Access the key from the 32-bit view of the Registry.
             WOW64: Access the key from the 64-bit view of the Registry.
         """
         WOWNative: _typing.ClassVar['WindowsRegistryManager.RegistryKeyName.RegistryKeyWowBitness'] = 'WOWNative'
         WOW32: _typing.ClassVar['WindowsRegistryManager.RegistryKeyName.RegistryKeyWowBitness'] = 'WOW32'
         WOW64: _typing.ClassVar['WindowsRegistryManager.RegistryKeyName.RegistryKeyWowBitness'] = 'WOW64'

      registryPath: str
      wowBitness: str

   class RegistryKey(pyVmomi.vmodl.DynamicData):
      """
      This describes the registry key.
      
      Attributes:
          keyName: The key name.
          classType: The user-defined class type of this key.
          lastWritten: Time stamp of last modification.
      """
      keyName: WindowsRegistryManager.RegistryKeyName
      classType: str
      lastWritten: _datetime.datetime

   class RegistryKeyRecord(pyVmomi.vmodl.DynamicData):
      """
      This describes the registry key record.
      
      Attributes:
          key: The key.
          fault: Any error that occurred while trying to access this key.
              
              Presence of this fault indicates that a recursive listing failed to
              open this key to find keys below it in the tree. This could be a
              result of insufficient user permissions within the guest.
      """
      key: WindowsRegistryManager.RegistryKey
      fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

   class RegistryValueName(pyVmomi.vmodl.DynamicData):
      """
      This describes the registry value name.
      
      Attributes:
          keyName: The key name that contains this value.
          name: The name of the value.
      """
      keyName: WindowsRegistryManager.RegistryKeyName
      name: str

   class RegistryValueData(pyVmomi.vmodl.DynamicData):
      """This describes the registry value data."""
      pass

   class RegistryValueDword(WindowsRegistryManager.RegistryValueData):
      """
      This describes the registry value dword.
      
      Attributes:
          value: The data of the registry value.
      """
      value: int

   class RegistryValueQword(WindowsRegistryManager.RegistryValueData):
      """
      This describes the registry value qword.
      
      Attributes:
          value: The data of the registry value.
      """
      value: pyVmomi.VmomiSupport.long

   class RegistryValueString(WindowsRegistryManager.RegistryValueData):
      """
      This describes the registry value string.
      
      Attributes:
          value: The data of the registry value.
              
              The Windows registry allows this type of value to exist without
              having any data associated with it.
      """
      value: _typing.Optional[str] = None

   class RegistryValueExpandString(WindowsRegistryManager.RegistryValueData):
      """
      This describes the registry value expand string.
      
      Attributes:
          value: The expanded (if applicable) data of the registry value.
              
              The Windows registry allows this type of value to exist without
              having any data associated with it.
      """
      value: _typing.Optional[str] = None

   class RegistryValueMultiString(WindowsRegistryManager.RegistryValueData):
      """
      This describes the registry value multi string.
      
      Attributes:
          value: The data of the registry value.
              
              The Windows registry allows this type of value to exist without
              having any data associated with it.
      """
      value: list[str] = []

   class RegistryValueBinary(WindowsRegistryManager.RegistryValueData):
      """
      This describes the registry value binary.
      
      Attributes:
          value: The data of the registry value.
              
              The Windows registry allows this type of value to exist without
              having any data associated with it.
      """
      value: _typing.Optional[pyVmomi.VmomiSupport.binary] = None

   class RegistryValue(pyVmomi.vmodl.DynamicData):
      """
      This describes the registry value.
      
      Attributes:
          name: The value name.
          data: The value data.
              
              Use one of the extended classes to specify data type:
              `pyVmomi.vim.vm.guest.WindowsRegistryManager.RegistryValueDword`,
              `pyVmomi.vim.vm.guest.WindowsRegistryManager.RegistryValueQword`,
              `pyVmomi.vim.vm.guest.WindowsRegistryManager.RegistryValueString`,
              `pyVmomi.vim.vm.guest.WindowsRegistryManager.RegistryValueExpandString`,
              `pyVmomi.vim.vm.guest.WindowsRegistryManager.RegistryValueMultiString`,
              `pyVmomi.vim.vm.guest.WindowsRegistryManager.RegistryValueBinary`.
      """
      name: WindowsRegistryManager.RegistryValueName
      data: WindowsRegistryManager.RegistryValueData

   def CreateRegistryKey(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, keyName: WindowsRegistryManager.RegistryKeyName, isVolatile: bool, classType: _typing.Optional[str]) -> None:
      """
      Create a registry key.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data.
          keyName: The path to the registry key to be created.
          isVolatile: If true, the key is created in memory and is not
              preserved across system reboot. Otherwise, it shall
              persist in the file system.
          classType: User defined class type for this key. May be omitted.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def ListRegistryKeys(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, keyName: WindowsRegistryManager.RegistryKeyName, recursive: bool, matchPattern: _typing.Optional[str]) -> list[WindowsRegistryManager.RegistryKeyRecord]:
      """
      List all registry subkeys for a given registry key.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data.
          keyName: The path to the registry key for which all subkeys are to
              be listed.
          recursive: If true, all subkeys are listed recursively.
          matchPattern: A filter for the key names returned, specified using
              perl-compatible regular expressions. If matchPattern
              is unset, then the pattern '.*' is used, which returns
              all key names found, otherwise only those key names
              that match the input pattern shall be returned.
      
      Returns:
          The list of subkeys is returned in an array of
          `pyVmomi.vim.vm.guest.WindowsRegistryManager.RegistryKey` structures.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def DeleteRegistryKey(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, keyName: WindowsRegistryManager.RegistryKeyName, recursive: bool) -> None:
      """
      Delete a registry key.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data.
          keyName: The path to the registry key to be deleted.
          recursive: If true, the key is deleted along with any subkeys (if
              present). Otherwise, it shall only delete the key if it
              has no subkeys.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def SetRegistryValue(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, value: WindowsRegistryManager.RegistryValue) -> None:
      """
      Set/Create a registry value.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data.
          value: The information for the registry value to be set/created.
              The Value \"name\" (specified in
              `pyVmomi.vim.vm.guest.WindowsRegistryManager.RegistryValueName`)
              and the Value \"data\" (specified in
              `pyVmomi.vim.vm.guest.WindowsRegistryManager.RegistryValue`)
              can both be empty. If \"name\" is empty, it sets the value for
              the unnamed or default value of the given key.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def ListRegistryValues(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, keyName: WindowsRegistryManager.RegistryKeyName, expandStrings: bool, matchPattern: _typing.Optional[str]) -> list[WindowsRegistryManager.RegistryValue]:
      """
      List all registry values for a given registry key.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data.
          keyName: The path to the registry key for which all values are to be
              listed.
          expandStrings: If true, all values that have expandable data such
              as environment variable names, shall get expanded in
              the result.
          matchPattern: A filter for the value names returned, specified using
              perl-compatible regular expressions. If matchPattern
              is unset, then the pattern '.*' is used, which returns
              all value names found, otherwise only those value
              names that match the input pattern shall be returned.
      
      Returns:
          The list of values is returned in an array of
          `pyVmomi.vim.vm.guest.WindowsRegistryManager.RegistryValue` structures.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def DeleteRegistryValue(self, vm: pyVmomi.vim.VirtualMachine, auth: GuestAuthentication, valueName: WindowsRegistryManager.RegistryValueName) -> None:
      """
      Delete a registry value.
      
      Args:
          vm: Virtual machine to perform the operation on.
          auth: The guest authentication data.
          valueName: The registry value name to be deleted.
              The Value \"name\" (specified in
              `pyVmomi.vim.vm.guest.WindowsRegistryManager.RegistryValueName`)
              can be empty. If \"name\" is empty, it deletes the value
              for the unnamed or default value of the given key.
      
      Raises:
          pyVmomi.vim.fault.GuestOperationsFault: if there is an error processing a guest
              operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
