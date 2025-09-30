# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vslm.AboutInfo import AboutInfo

from pyVmomi.vslm.StorageLifecycleManager import StorageLifecycleManager

from pyVmomi.vslm.auth.SessionManager import SessionManager

from pyVmomi.vslm.vso.VStorageObjectManager import VStorageObjectManager

class ServiceInstanceContent(DynamicData):
   aboutInfo: AboutInfo
   sessionManager: SessionManager
   vStorageObjectManager: VStorageObjectManager
   storageLifecycleManager: StorageLifecycleManager
