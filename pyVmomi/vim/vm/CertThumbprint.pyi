# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class CertThumbprint(DynamicData):
   class HashAlgorithm(Enum):
      sha256: ClassVar['HashAlgorithm'] = 'sha256'

   thumbprint: str
   hashAlgorithm: Optional[str] = None
