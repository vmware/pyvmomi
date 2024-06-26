# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import ComputeResource
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.vm.device import VirtualDiskId

class IoFilterManager(ManagedObject):
   class IoFilterInfo(DynamicData):
      id: str
      name: str
      vendor: str
      version: str
      type: Optional[str] = None
      summary: Optional[str] = None
      releaseDate: Optional[str] = None

   class HostIoFilterInfo(IoFilterInfo):
      available: bool

   class OperationType(Enum):
      install: ClassVar['OperationType'] = 'install'
      uninstall: ClassVar['OperationType'] = 'uninstall'
      upgrade: ClassVar['OperationType'] = 'upgrade'

   class ClusterIoFilterInfo(IoFilterInfo):
      opType: str
      vibUrl: Optional[str] = None

   class IoFilterType(Enum):
      cache: ClassVar['IoFilterType'] = 'cache'
      replication: ClassVar['IoFilterType'] = 'replication'
      encryption: ClassVar['IoFilterType'] = 'encryption'
      compression: ClassVar['IoFilterType'] = 'compression'
      inspection: ClassVar['IoFilterType'] = 'inspection'
      datastoreIoControl: ClassVar['IoFilterType'] = 'datastoreIoControl'
      dataProvider: ClassVar['IoFilterType'] = 'dataProvider'
      dataCapture: ClassVar['IoFilterType'] = 'dataCapture'

   class SslTrust(DynamicData):
      pass

   class PinnedCertificate(SslTrust):
      sslCertificate: str

   class UntrustedCertificate(SslTrust):
      pass

   class QueryIssueResult(DynamicData):
      class HostIssue(DynamicData):
         host: HostSystem
         issue: list[MethodFault] = []

      opType: str
      hostIssue: list[HostIssue] = []

   def InstallIoFilter(self, vibUrl: str, compRes: ComputeResource, vibSslTrust: Optional[SslTrust]) -> Task: ...
   def UninstallIoFilter(self, filterId: str, compRes: ComputeResource) -> Task: ...
   def UpgradeIoFilter(self, filterId: str, compRes: ComputeResource, vibUrl: str, vibSslTrust: Optional[SslTrust]) -> Task: ...
   def QueryIssue(self, filterId: str, compRes: ComputeResource) -> QueryIssueResult: ...
   def QueryIoFilterInfo(self, compRes: ComputeResource) -> list[ClusterIoFilterInfo]: ...
   def ResolveInstallationErrorsOnHost(self, filterId: str, host: HostSystem) -> Task: ...
   def ResolveInstallationErrorsOnCluster(self, filterId: str, cluster: ClusterComputeResource) -> Task: ...
   def QueryDisksUsingFilter(self, filterId: str, compRes: ComputeResource) -> list[VirtualDiskId]: ...
