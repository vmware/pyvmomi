# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ExtendedElementDescription
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

class Profile(ManagedObject):
   class CreateSpec(DynamicData):
      name: Optional[str] = None
      annotation: Optional[str] = None
      enabled: Optional[bool] = None

   class SerializedCreateSpec(CreateSpec):
      profileConfigString: str

   class ConfigInfo(DynamicData):
      name: str
      annotation: Optional[str] = None
      enabled: bool

   class Description(DynamicData):
      class Section(DynamicData):
         description: ExtendedElementDescription
         message: list[LocalizableMessage] = []

      section: list[Section] = []

   @property
   def config(self) -> ConfigInfo: ...
   @property
   def description(self) -> Optional[Description]: ...
   @property
   def name(self) -> str: ...
   @property
   def createdTime(self) -> datetime: ...
   @property
   def modifiedTime(self) -> datetime: ...
   @property
   def entity(self) -> list[ManagedEntity]: ...
   @property
   def complianceStatus(self) -> str: ...

   def RetrieveDescription(self) -> Optional[Description]: ...
   def Destroy(self) -> NoReturn: ...
   def AssociateEntities(self, entity: list[ManagedEntity]) -> NoReturn: ...
   def DissociateEntities(self, entity: list[ManagedEntity]) -> NoReturn: ...
   def CheckCompliance(self, entity: list[ManagedEntity]) -> Task: ...
   def ExportProfile(self) -> str: ...
