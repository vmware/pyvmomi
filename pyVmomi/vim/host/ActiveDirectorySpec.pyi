# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class ActiveDirectorySpec(DynamicData):
   class Specification(DynamicData):
      domainName: Optional[str] = None
      userName: Optional[str] = None
      password: Optional[str] = None
      camServer: Optional[str] = None
      thumbprint: Optional[str] = None
      certificate: Optional[str] = None
      smartCardAuthenticationEnabled: Optional[bool] = None
      smartCardTrustAnchors: list[str] = []

   changeOperation: str
   spec: Optional[Specification] = None
