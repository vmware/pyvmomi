# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class SoftwarePackage(DynamicData):
   class VibType(Enum):
      bootbank: ClassVar['VibType'] = 'bootbank'
      tools: ClassVar['VibType'] = 'tools'
      meta: ClassVar['VibType'] = 'meta'

   class Capability(DynamicData):
      liveInstallAllowed: Optional[bool] = None
      liveRemoveAllowed: Optional[bool] = None
      statelessReady: Optional[bool] = None
      overlay: Optional[bool] = None

   class Constraint(Enum):
      equals: ClassVar['Constraint'] = 'equals'
      lessThan: ClassVar['Constraint'] = 'lessThan'
      lessThanEqual: ClassVar['Constraint'] = 'lessThanEqual'
      greaterThanEqual: ClassVar['Constraint'] = 'greaterThanEqual'
      greaterThan: ClassVar['Constraint'] = 'greaterThan'

   class Relation(DynamicData):
      constraint: Optional[str] = None
      name: str
      version: Optional[str] = None

   name: str
   version: str
   type: str
   vendor: str
   acceptanceLevel: str
   summary: str
   description: str
   referenceURL: list[str] = []
   creationDate: Optional[datetime] = None
   depends: list[Relation] = []
   conflicts: list[Relation] = []
   replaces: list[Relation] = []
   provides: list[str] = []
   maintenanceModeRequired: Optional[bool] = None
   hardwarePlatformsRequired: list[str] = []
   capability: Capability
   tag: list[str] = []
   payload: list[str] = []
