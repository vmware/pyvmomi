# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.pbm.profile import CapabilityConstraints
from pyVmomi.pbm.profile import Profile
from pyVmomi.pbm.profile import ResourceType

class CapabilityBasedProfile(Profile):
   class ProfileCategoryEnum(Enum):
      REQUIREMENT: ClassVar['ProfileCategoryEnum'] = 'REQUIREMENT'
      RESOURCE: ClassVar['ProfileCategoryEnum'] = 'RESOURCE'
      DATA_SERVICE_POLICY: ClassVar['ProfileCategoryEnum'] = 'DATA_SERVICE_POLICY'

   class SystemCreatedProfileType(Enum):
      VsanDefaultProfile: ClassVar['SystemCreatedProfileType'] = 'VsanDefaultProfile'
      VVolDefaultProfile: ClassVar['SystemCreatedProfileType'] = 'VVolDefaultProfile'
      PmemDefaultProfile: ClassVar['SystemCreatedProfileType'] = 'PmemDefaultProfile'
      VmcManagementProfile: ClassVar['SystemCreatedProfileType'] = 'VmcManagementProfile'
      VsanMaxDefaultProfile: ClassVar['SystemCreatedProfileType'] = 'VsanMaxDefaultProfile'

   profileCategory: str
   resourceType: ResourceType
   constraints: CapabilityConstraints
   generationId: Optional[long] = None
   isDefault: bool
   systemCreatedProfileType: Optional[str] = None
   lineOfService: Optional[str] = None
