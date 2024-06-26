# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class ServiceLocator(DynamicData):
   class Credential(DynamicData):
      pass

   class NamePassword(Credential):
      username: str
      password: str

   class SAMLCredential(Credential):
      token: Optional[str] = None

   instanceUuid: str
   url: str
   credential: Credential
   sslThumbprint: Optional[str] = None
