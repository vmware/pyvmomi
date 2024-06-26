# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import byte

from pyVmomi.vmodl import DynamicData

class DigestInfo(DynamicData):
   class DigestMethodType(Enum):
      SHA1: ClassVar['DigestMethodType'] = 'SHA1'
      MD5: ClassVar['DigestMethodType'] = 'MD5'
      SHA256: ClassVar['DigestMethodType'] = 'SHA256'
      SHA384: ClassVar['DigestMethodType'] = 'SHA384'
      SHA512: ClassVar['DigestMethodType'] = 'SHA512'
      SM3_256: ClassVar['DigestMethodType'] = 'SM3_256'

   digestMethod: str
   digestValue: list[byte] = []
   objectName: Optional[str] = None
