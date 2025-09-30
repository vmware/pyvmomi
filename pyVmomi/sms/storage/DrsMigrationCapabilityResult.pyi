# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.sms.storage.DatastorePair import DatastorePair

class DrsMigrationCapabilityResult(DynamicData):
   recommendedDatastorePair: list[DatastorePair] = []
   nonRecommendedDatastorePair: list[DatastorePair] = []
