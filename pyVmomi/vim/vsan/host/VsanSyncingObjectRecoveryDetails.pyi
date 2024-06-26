# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class VsanSyncingObjectRecoveryDetails(DynamicData):
   activelySyncingObjectRecoveryETA: Optional[long] = None
   queuedForSyncObjectRecoveryETA: Optional[long] = None
   suspendedObjectRecoveryETA: Optional[long] = None
   activeObjectsToSync: Optional[long] = None
   queuedObjectsToSync: Optional[long] = None
   suspendedObjectsToSync: Optional[long] = None
   bytesToSyncForActiveObjects: Optional[long] = None
   bytesToSyncForQueuedObjects: Optional[long] = None
   bytesToSyncForSuspendedObjects: Optional[long] = None
