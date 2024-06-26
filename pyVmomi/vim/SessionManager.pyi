# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedMethod
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import UserSession

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm import CertThumbprint

class SessionManager(ManagedObject):
   class LocalTicket(DynamicData):
      userName: str
      passwordFilePath: str

   class GenericServiceTicket(DynamicData):
      class TicketType(Enum):
         HttpNfcServiceTicket: ClassVar['TicketType'] = 'HttpNfcServiceTicket'
         HostServiceTicket: ClassVar['TicketType'] = 'HostServiceTicket'
         VcServiceTicket: ClassVar['TicketType'] = 'VcServiceTicket'

      id: str
      hostName: Optional[str] = None
      sslThumbprint: Optional[str] = None
      certThumbprintList: list[CertThumbprint] = []
      ticketType: Optional[str] = None

   class ServiceRequestSpec(DynamicData):
      pass

   class VmomiServiceRequestSpec(ServiceRequestSpec):
      method: ManagedMethod

   class HttpServiceRequestSpec(ServiceRequestSpec):
      class Method(Enum):
         httpOptions: ClassVar['Method'] = 'httpOptions'
         httpGet: ClassVar['Method'] = 'httpGet'
         httpHead: ClassVar['Method'] = 'httpHead'
         httpPost: ClassVar['Method'] = 'httpPost'
         httpPut: ClassVar['Method'] = 'httpPut'
         httpDelete: ClassVar['Method'] = 'httpDelete'
         httpTrace: ClassVar['Method'] = 'httpTrace'
         httpConnect: ClassVar['Method'] = 'httpConnect'

      method: Optional[str] = None
      url: str

   @property
   def sessionList(self) -> list[UserSession]: ...
   @property
   def currentSession(self) -> Optional[UserSession]: ...
   @property
   def message(self) -> Optional[str]: ...
   @property
   def messageLocaleList(self) -> list[str]: ...
   @property
   def supportedLocaleList(self) -> list[str]: ...
   @property
   def defaultLocale(self) -> str: ...

   def UpdateMessage(self, message: str) -> NoReturn: ...
   def LoginByToken(self, locale: Optional[str]) -> UserSession: ...
   def Login(self, userName: str, password: str, locale: Optional[str]) -> UserSession: ...
   def LoginBySSPI(self, base64Token: str, locale: Optional[str]) -> UserSession: ...
   def Logout(self) -> NoReturn: ...
   def AcquireLocalTicket(self, userName: str) -> LocalTicket: ...
   def AcquireGenericServiceTicket(self, spec: ServiceRequestSpec) -> GenericServiceTicket: ...
   def Terminate(self, sessionId: list[str]) -> NoReturn: ...
   def SetLocale(self, locale: str) -> NoReturn: ...
   def LoginExtensionBySubjectName(self, extensionKey: str, locale: Optional[str]) -> UserSession: ...
   def LoginExtensionByCertificate(self, extensionKey: str, locale: Optional[str]) -> UserSession: ...
   def ImpersonateUser(self, userName: str, locale: Optional[str]) -> UserSession: ...
   def SessionIsActive(self, sessionID: str, userName: str) -> bool: ...
   def AcquireCloneTicket(self) -> str: ...
   def CloneSession(self, cloneTicket: str) -> UserSession: ...
