# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VimVasaProvider(DynamicData):
   class StatePerArray(DynamicData):
      priority: int
      arrayId: str
      active: bool

   class VirtualHostConfig(DynamicData):
      vhostName: Optional[str] = None
      serviceHost: str
      servicePort: Optional[int] = None

   uid: Optional[str] = None
   url: str
   name: Optional[str] = None
   selfSignedCertificate: Optional[str] = None
   vhostConfig: Optional[VirtualHostConfig] = None
   versionId: Optional[int] = None
