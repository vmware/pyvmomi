# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.sms import EntityReference

from pyVmomi.vmodl.fault import InvalidArgument

class QueryNotSupported(InvalidArgument):
   entityType: Optional[EntityReference.EntityType] = None
   relatedEntityType: EntityReference.EntityType
