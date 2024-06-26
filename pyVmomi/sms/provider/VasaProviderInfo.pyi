# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.sms.provider import ProviderInfo

class VasaProviderInfo(ProviderInfo):
   class CertificateStatus(Enum):
      valid: ClassVar['CertificateStatus'] = 'valid'
      expirySoftLimitReached: ClassVar['CertificateStatus'] = 'expirySoftLimitReached'
      expiryHardLimitReached: ClassVar['CertificateStatus'] = 'expiryHardLimitReached'
      expired: ClassVar['CertificateStatus'] = 'expired'
      invalid: ClassVar['CertificateStatus'] = 'invalid'

   class RelatedStorageArray(DynamicData):
      arrayId: str
      active: bool
      manageable: bool
      priority: int

   class SupportedVendorModelMapping(DynamicData):
      vendorId: Optional[str] = None
      modelId: Optional[str] = None

   class VasaProviderStatus(Enum):
      online: ClassVar['VasaProviderStatus'] = 'online'
      offline: ClassVar['VasaProviderStatus'] = 'offline'
      syncError: ClassVar['VasaProviderStatus'] = 'syncError'
      unknown: ClassVar['VasaProviderStatus'] = 'unknown'
      connected: ClassVar['VasaProviderStatus'] = 'connected'
      disconnected: ClassVar['VasaProviderStatus'] = 'disconnected'

   class VasaProviderProfile(Enum):
      blockDevice: ClassVar['VasaProviderProfile'] = 'blockDevice'
      fileSystem: ClassVar['VasaProviderProfile'] = 'fileSystem'
      capability: ClassVar['VasaProviderProfile'] = 'capability'

   class ProviderProfile(Enum):
      ProfileBasedManagement: ClassVar['ProviderProfile'] = 'ProfileBasedManagement'
      Replication: ClassVar['ProviderProfile'] = 'Replication'

   class Type(Enum):
      PERSISTENCE: ClassVar['Type'] = 'PERSISTENCE'
      DATASERVICE: ClassVar['Type'] = 'DATASERVICE'
      UNKNOWN: ClassVar['Type'] = 'UNKNOWN'

   class Category(Enum):
      internal: ClassVar['Category'] = 'internal'
      external: ClassVar['Category'] = 'external'

   url: str
   certificate: Optional[str] = None
   status: Optional[str] = None
   statusFault: Optional[MethodFault] = None
   vasaVersion: Optional[str] = None
   namespace: Optional[str] = None
   lastSyncTime: Optional[str] = None
   supportedVendorModelMapping: list[SupportedVendorModelMapping] = []
   supportedProfile: list[str] = []
   supportedProviderProfile: list[str] = []
   relatedStorageArray: list[RelatedStorageArray] = []
   providerId: Optional[str] = None
   certificateExpiryDate: Optional[str] = None
   certificateStatus: Optional[str] = None
   serviceLocation: Optional[str] = None
   needsExplicitActivation: Optional[bool] = None
   maxBatchSize: Optional[long] = None
   retainVasaProviderCertificate: Optional[bool] = None
   arrayIndependentProvider: Optional[bool] = None
   type: Optional[str] = None
   category: Optional[str] = None
   priority: Optional[int] = None
   failoverGroupId: Optional[str] = None
