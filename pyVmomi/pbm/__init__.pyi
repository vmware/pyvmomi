# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import auth as auth
from . import capability as capability
from . import compliance as compliance
from . import fault as fault
from . import placement as placement
from . import profile as profile
from . import provider as provider
from . import replication as replication

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vmodl
import pyVmomi.pbm.auth
import pyVmomi.pbm.capability
import pyVmomi.pbm.compliance
import pyVmomi.pbm.placement
import pyVmomi.pbm.profile
import pyVmomi.pbm.replication



class AboutInfo(pyVmomi.vmodl.DynamicData):
   name: str
   version: str
   instanceUuid: str


class ExtendedElementDescription(pyVmomi.vmodl.DynamicData):
   label: str
   summary: str
   key: str
   messageCatalogKeyPrefix: str
   messageArg: list[pyVmomi.vmodl.KeyAnyValue] = []


class LoggingConfiguration(pyVmomi.vmodl.DynamicData):
   class Component(pyVmomi.VmomiSupport.Enum):
      pbm: _typing.ClassVar['Component'] = 'pbm'
      vslm: _typing.ClassVar['Component'] = 'vslm'
      sms: _typing.ClassVar['Component'] = 'sms'
      spbm: _typing.ClassVar['Component'] = 'spbm'
      sps: _typing.ClassVar['Component'] = 'sps'
      httpclient_header: _typing.ClassVar['Component'] = 'httpclient_header'
      httpclient_content: _typing.ClassVar['Component'] = 'httpclient_content'
      vmomi: _typing.ClassVar['Component'] = 'vmomi'

   class LogLevel(pyVmomi.VmomiSupport.Enum):
      INFO: _typing.ClassVar['LogLevel'] = 'INFO'
      DEBUG: _typing.ClassVar['LogLevel'] = 'DEBUG'
      TRACE: _typing.ClassVar['LogLevel'] = 'TRACE'

   component: str
   logLevel: str


class ServerObjectRef(pyVmomi.vmodl.DynamicData):
   class VvolType(pyVmomi.VmomiSupport.Enum):
      Config: _typing.ClassVar['VvolType'] = 'Config'
      Data: _typing.ClassVar['VvolType'] = 'Data'
      Swap: _typing.ClassVar['VvolType'] = 'Swap'

   class ObjectType(pyVmomi.VmomiSupport.Enum):
      virtualMachine: _typing.ClassVar['ObjectType'] = 'virtualMachine'
      virtualMachineAndDisks: _typing.ClassVar['ObjectType'] = 'virtualMachineAndDisks'
      virtualDiskId: _typing.ClassVar['ObjectType'] = 'virtualDiskId'
      virtualDiskUUID: _typing.ClassVar['ObjectType'] = 'virtualDiskUUID'
      datastore: _typing.ClassVar['ObjectType'] = 'datastore'
      vsanObjectId: _typing.ClassVar['ObjectType'] = 'vsanObjectId'
      fileShareId: _typing.ClassVar['ObjectType'] = 'fileShareId'
      host: _typing.ClassVar['ObjectType'] = 'host'
      cluster: _typing.ClassVar['ObjectType'] = 'cluster'
      unknown: _typing.ClassVar['ObjectType'] = 'unknown'

   objectType: str
   key: str
   serverUuid: _typing.Optional[str] = None


class ServiceInstance(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def content(self) -> ServiceInstanceContent: ...

   def RetrieveContent(self) -> ServiceInstanceContent: ...


class ServiceInstanceContent(pyVmomi.vmodl.DynamicData):
   aboutInfo: AboutInfo
   sessionManager: pyVmomi.pbm.auth.SessionManager
   capabilityMetadataManager: pyVmomi.pbm.capability.CapabilityMetadataManager
   profileManager: pyVmomi.pbm.profile.ProfileManager
   complianceManager: pyVmomi.pbm.compliance.ComplianceManager
   placementSolver: pyVmomi.pbm.placement.PlacementSolver
   replicationManager: _typing.Optional[pyVmomi.pbm.replication.ReplicationManager] = None
