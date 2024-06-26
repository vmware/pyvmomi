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

from pyVmomi.vmodl import DynamicData

class CertificateManager(ManagedObject):
   class CertificateKind(Enum):
      Machine: ClassVar['CertificateKind'] = 'Machine'
      VASAClient: ClassVar['CertificateKind'] = 'VASAClient'

   class CertificateSpec(DynamicData):
      kind: str

   class CertificateInfo(DynamicData):
      class CertificateStatus(Enum):
         unknown: ClassVar['CertificateStatus'] = 'unknown'
         expired: ClassVar['CertificateStatus'] = 'expired'
         expiring: ClassVar['CertificateStatus'] = 'expiring'
         expiringShortly: ClassVar['CertificateStatus'] = 'expiringShortly'
         expirationImminent: ClassVar['CertificateStatus'] = 'expirationImminent'
         good: ClassVar['CertificateStatus'] = 'good'

      kind: Optional[str] = None
      issuer: Optional[str] = None
      notBefore: Optional[datetime] = None
      notAfter: Optional[datetime] = None
      subject: Optional[str] = None
      status: str

   @property
   def certificateInfo(self) -> CertificateInfo: ...

   def RetrieveCertificateInfoList(self) -> list[CertificateInfo]: ...
   def GenerateCertificateSigningRequest(self, useIpAddressAsCommonName: bool, spec: Optional[CertificateSpec]) -> str: ...
   def GenerateCertificateSigningRequestByDn(self, distinguishedName: str, spec: Optional[CertificateSpec]) -> str: ...
   def ProvisionServerPrivateKey(self, key: str) -> NoReturn: ...
   def InstallServerCertificate(self, cert: str) -> NoReturn: ...
   def ReplaceCACertificatesAndCRLs(self, caCert: list[str], caCrl: list[str]) -> NoReturn: ...
   def NotifyAffectedServices(self, services: list[str]) -> NoReturn: ...
   def ListCACertificates(self) -> list[str]: ...
   def ListCACertificateRevocationLists(self) -> list[str]: ...
