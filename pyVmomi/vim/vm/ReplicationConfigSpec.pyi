# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class ReplicationConfigSpec(DynamicData):
   class DiskSettings(DynamicData):
      key: int
      diskReplicationId: str

   generation: long
   vmReplicationId: str
   destination: str
   port: int
   rpo: long
   quiesceGuestEnabled: bool
   paused: bool
   oppUpdatesEnabled: bool
   netCompressionEnabled: Optional[bool] = None
   netEncryptionEnabled: Optional[bool] = None
   encryptionDestination: Optional[str] = None
   encryptionPort: Optional[int] = None
   remoteCertificateThumbprint: Optional[str] = None
   dataSetsReplicationEnabled: Optional[bool] = None
   disk: list[DiskSettings] = []
