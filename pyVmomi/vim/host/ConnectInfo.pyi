# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Datastore
from pyVmomi.vim import LicenseManager
from pyVmomi.vim import Network

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import Capability
from pyVmomi.vim.host import Summary

from pyVmomi.vim.vm import Summary

class ConnectInfo(DynamicData):
   class NetworkInfo(DynamicData):
      summary: Network.Summary

   class NewNetworkInfo(NetworkInfo):
      pass

   class DatastoreInfo(DynamicData):
      summary: Datastore.Summary

   class DatastoreExistsInfo(DatastoreInfo):
      newDatastoreName: str

   class DatastoreNameConflictInfo(DatastoreInfo):
      newDatastoreName: str

   class LicenseInfo(DynamicData):
      license: LicenseManager.LicenseInfo
      evaluation: LicenseManager.EvaluationInfo
      resource: Optional[LicenseManager.LicensableResourceInfo] = None

   serverIp: Optional[str] = None
   inDasCluster: Optional[bool] = None
   host: Summary
   vm: list[Summary] = []
   vimAccountNameRequired: Optional[bool] = None
   clusterSupported: Optional[bool] = None
   network: list[NetworkInfo] = []
   datastore: list[DatastoreInfo] = []
   license: Optional[LicenseInfo] = None
   capability: Optional[Capability] = None
