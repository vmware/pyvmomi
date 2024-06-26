# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.pbm.profile import ProfileId

class Profile(DynamicData):
   profileId: ProfileId
   name: str
   description: Optional[str] = None
   creationTime: datetime
   createdBy: str
   lastUpdatedTime: datetime
   lastUpdatedBy: str
