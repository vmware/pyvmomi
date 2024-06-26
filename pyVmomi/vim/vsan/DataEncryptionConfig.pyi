# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.encryption import KeyProviderId

class DataEncryptionConfig(DynamicData):
   encryptionEnabled: bool
   kmsProviderId: Optional[KeyProviderId] = None
   kekId: Optional[str] = None
   hostKeyId: Optional[str] = None
   dekGenerationId: Optional[long] = None
   changing: Optional[bool] = None
   eraseDisksBeforeUse: Optional[bool] = None
   wrappedDek: Optional[str] = None
   dekId: Optional[str] = None
   oldWrappedDek: Optional[str] = None
   oldDekId: Optional[str] = None
   kekVerifier: Optional[str] = None
   dekVerifier: Optional[str] = None
   oldDekVerifier: Optional[str] = None
   iv: Optional[str] = None
   syncing: Optional[bool] = None
