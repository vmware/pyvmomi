# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.sms.provider import ProviderInfo

from pyVmomi.sms.storage import StorageContainer

class StorageContainerResult(DynamicData):
   storageContainer: list[StorageContainer] = []
   providerInfo: list[ProviderInfo] = []
