# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import DynamicData

class EntityConfigInfo(DynamicData):
   class Action(Enum):
      none: ClassVar['Action'] = 'none'
      powerOn: ClassVar['Action'] = 'powerOn'
      powerOff: ClassVar['Action'] = 'powerOff'
      guestShutdown: ClassVar['Action'] = 'guestShutdown'
      suspend: ClassVar['Action'] = 'suspend'

   key: Optional[ManagedEntity] = None
   tag: Optional[str] = None
   startOrder: Optional[int] = None
   startDelay: Optional[int] = None
   waitingForGuest: Optional[bool] = None
   startAction: Optional[str] = None
   stopDelay: Optional[int] = None
   stopAction: Optional[str] = None
   destroyWithParent: Optional[bool] = None
