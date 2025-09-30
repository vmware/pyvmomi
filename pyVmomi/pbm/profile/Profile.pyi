# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.pbm.profile.ProfileId import ProfileId

class Profile(DynamicData):
   profileId: ProfileId
   name: str
   description: Optional[str] = None
   creationTime: datetime
   createdBy: str
   lastUpdatedTime: datetime
   lastUpdatedBy: str
