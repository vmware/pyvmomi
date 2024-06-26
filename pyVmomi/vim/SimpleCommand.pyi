# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ServiceManager

class SimpleCommand(ManagedObject):
   class Encoding(Enum):
      CSV: ClassVar['Encoding'] = 'CSV'
      HEX: ClassVar['Encoding'] = 'HEX'
      STRING: ClassVar['Encoding'] = 'STRING'

   @property
   def encodingType(self) -> Encoding: ...
   @property
   def entity(self) -> ServiceManager.ServiceInfo: ...

   def Execute(self, arguments: list[str]) -> str: ...
