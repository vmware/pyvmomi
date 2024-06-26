# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ElementDescription
from pyVmomi.vim import EnumDescription

from pyVmomi.vmodl import DynamicData

class EventDescription(DynamicData):
   class EventCategory(Enum):
      info: ClassVar['EventCategory'] = 'info'
      warning: ClassVar['EventCategory'] = 'warning'
      error: ClassVar['EventCategory'] = 'error'
      user: ClassVar['EventCategory'] = 'user'

   class EventArgDesc(DynamicData):
      name: str
      type: str
      description: Optional[ElementDescription] = None

   class EventDetail(DynamicData):
      key: type
      description: Optional[str] = None
      category: str
      formatOnDatacenter: str
      formatOnComputeResource: str
      formatOnHost: str
      formatOnVm: str
      fullFormat: str
      longDescription: Optional[str] = None

   category: list[ElementDescription] = []
   eventInfo: list[EventDetail] = []
   enumeratedTypes: list[EnumDescription] = []
