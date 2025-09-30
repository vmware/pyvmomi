# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.Network import Network

from pyVmomi.vmodl.DynamicData import DynamicData

class EsxAgentHostManager(ManagedObject):
   class ConfigInfo(DynamicData):
      agentVmDatastore: Optional[Datastore] = None
      agentVmNetwork: Optional[Network] = None

   @property
   def configInfo(self) -> ConfigInfo: ...

   def UpdateConfig(self, configInfo: ConfigInfo) -> None: ...
