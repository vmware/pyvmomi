# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl import DynamicData

from pyVmomi.vslm import AboutInfo
from pyVmomi.vslm import StorageLifecycleManager

from pyVmomi.vslm.auth import SessionManager

from pyVmomi.vslm.vso import VStorageObjectManager

class ServiceInstanceContent(DynamicData):
   aboutInfo: AboutInfo
   sessionManager: SessionManager
   vStorageObjectManager: VStorageObjectManager
   storageLifecycleManager: StorageLifecycleManager
