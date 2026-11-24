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
   """
   The `pyVmomi.pbm.AboutInfo` data object stores identifying data
   about the Storage Policy Server.
   
   Attributes:
       name: Name of the server.
       version: Version number.
       instanceUuid: Globally unique identifier associated with this server instance.
   """
   name: str
   version: str
   instanceUuid: str


class ExtendedElementDescription(pyVmomi.vmodl.DynamicData):
   """
   Attributes:
       label: Display label.
       summary: Summary description.
       key: Enumeration or literal ID being described.
       messageCatalogKeyPrefix: Key to the localized message string in the catalog.
           
           If the localized string contains parameters, values to the
           parameters will be provided in #messageArg.
           E.g: If the message in the catalog is
           \"IP address is {address}\", value for \"address\"
           will be provided by #messageArg.
           Both summary and label in ElementDescription will have a corresponding
           entry in the message catalog with the keys
           <messageCatalogKeyPrefix>.summary and <messageCatalogKeyPrefix>.label
           respectively.
           ElementDescription.summary and ElementDescription.label will contain
           the strings in server locale.
       messageArg: Provides named arguments that can be used to localize the
           message in the catalog.
   """
   label: str
   summary: str
   key: str
   messageCatalogKeyPrefix: str
   messageArg: list[pyVmomi.vmodl.KeyAnyValue] = []


class LoggingConfiguration(pyVmomi.vmodl.DynamicData):
   class Component(pyVmomi.VmomiSupport.Enum):
      """
      This enum corresponds to the different packages whose logging
      is configured independently by sps service.
      
      Attributes:
          pbm: Modifies logging level of com.vmware.pbm package.
          vslm: Modifies logging level of com.vmware.vslm package.
          sms: Modifies logging level of com.vmware.vim.sms package.
          spbm: Modifies logging level of com.vmware.spbm package.
          sps: Modifies logging level of com.vmware.sps package.
          httpclient_header: Modifies logging level of httpclient wire header.
          httpclient_content: Modifies logging level of httpclient wire content.
          vmomi: Modifies logging level of com.vmware.vim.vmomi package.
      """
      pbm: _typing.ClassVar['LoggingConfiguration.Component'] = 'pbm'
      vslm: _typing.ClassVar['LoggingConfiguration.Component'] = 'vslm'
      sms: _typing.ClassVar['LoggingConfiguration.Component'] = 'sms'
      spbm: _typing.ClassVar['LoggingConfiguration.Component'] = 'spbm'
      sps: _typing.ClassVar['LoggingConfiguration.Component'] = 'sps'
      httpclient_header: _typing.ClassVar['LoggingConfiguration.Component'] = 'httpclient_header'
      httpclient_content: _typing.ClassVar['LoggingConfiguration.Component'] = 'httpclient_content'
      vmomi: _typing.ClassVar['LoggingConfiguration.Component'] = 'vmomi'

   class LogLevel(pyVmomi.VmomiSupport.Enum):
      """
      This enum corresponds to the different log levels supported
      by sps service.
      
      Attributes:
          INFO: Refers to INFO level logging
          DEBUG: Refers to DEBUG level logging.
          TRACE: Refers to TRACE level logging.
      """
      INFO: _typing.ClassVar['LoggingConfiguration.LogLevel'] = 'INFO'
      DEBUG: _typing.ClassVar['LoggingConfiguration.LogLevel'] = 'DEBUG'
      TRACE: _typing.ClassVar['LoggingConfiguration.LogLevel'] = 'TRACE'

   component: str
   logLevel: str


class ServerObjectRef(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.ServerObjectRef` data object identifies
   a virtual machine,
   virtual disk attached to a virtual machine,
   a first class storage object
   or a datastore.
   
   Attributes:
       objectType: Type of vSphere Server object.
           
           The value of the `objectType` string
           corresponds to one of the `pyVmomi.pbm.ServerObjectRef.ObjectType`
           enumerated type values.
       key: Unique identifier for the object.
           
           The value of `key` depends
           on the `objectType`.
             
             
           PbmObjectType - key value
           
           virtualMachine - virtual-machine-MOR
           
           virtualDiskId
            - virtual-disk-MOR:VirtualDisk.key
           
           datastore - datastore-MOR
           
           MOR = ManagedObjectReference
       serverUuid: vCenter Server UUID; the `ServiceContent.about.instanceUuid`
           property in the vSphere API.
   """
   class VvolType(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.pbm.ServerObjectRef.VvolType` enumeration type
      defines VVOL types.
      
      VvolType's are referenced to specify which objectType
      to fetch for default capability.
      
      Attributes:
          Config: meta-data volume
          Data: vmdk volume
          Swap: swap volume
      """
      Config: _typing.ClassVar['ServerObjectRef.VvolType'] = 'Config'
      Data: _typing.ClassVar['ServerObjectRef.VvolType'] = 'Data'
      Swap: _typing.ClassVar['ServerObjectRef.VvolType'] = 'Swap'

   class ObjectType(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.pbm.ServerObjectRef.ObjectType` enumerated type
      defines vSphere Server object types that are known
      to the Storage Policy Server.
      
      See `pyVmomi.pbm.ServerObjectRef`.`pyVmomi.pbm.ServerObjectRef.objectType`.
      
      Attributes:
          virtualMachine: Indicates a virtual machine, not including the disks, identified by the virtual machine
              identifier virtual-machine-mor.
          virtualMachineAndDisks: Indicates the virtual machine and all its disks, identified by the virtual machine
              identifier virtual-machine-mor.
          virtualDiskId: Indicates a virtual disk, identified by disk key
              (virtual-machine-mor:disk-key).
          virtualDiskUUID: Indicates a virtual disk, identified by UUID - for First Class Storage Object support.
          datastore: Indicates a datastore.
          vsanObjectId: Indicates a VSAN object
          fileShareId: Indicates a file service
          host: Indicates a host.
          cluster: Indicates a cluster.
          unknown: Unknown object type.
      """
      virtualMachine: _typing.ClassVar['ServerObjectRef.ObjectType'] = 'virtualMachine'
      virtualMachineAndDisks: _typing.ClassVar['ServerObjectRef.ObjectType'] = 'virtualMachineAndDisks'
      virtualDiskId: _typing.ClassVar['ServerObjectRef.ObjectType'] = 'virtualDiskId'
      virtualDiskUUID: _typing.ClassVar['ServerObjectRef.ObjectType'] = 'virtualDiskUUID'
      datastore: _typing.ClassVar['ServerObjectRef.ObjectType'] = 'datastore'
      vsanObjectId: _typing.ClassVar['ServerObjectRef.ObjectType'] = 'vsanObjectId'
      fileShareId: _typing.ClassVar['ServerObjectRef.ObjectType'] = 'fileShareId'
      host: _typing.ClassVar['ServerObjectRef.ObjectType'] = 'host'
      cluster: _typing.ClassVar['ServerObjectRef.ObjectType'] = 'cluster'
      unknown: _typing.ClassVar['ServerObjectRef.ObjectType'] = 'unknown'

   objectType: str
   key: str
   serverUuid: _typing.Optional[str] = None


class ServiceInstance(pyVmomi.VmomiSupport.ManagedObject):
   """
   The `pyVmomi.pbm.ServiceInstance` managed object is the root object of the
   Storage Policy service.
   
   After you connect to the Storage Policy Server,
   you create a reference to the `pyVmomi.pbm.ServiceInstance`, and use
   that reference to retrieve the `pyVmomi.pbm.ServiceInstanceContent`
   data object. The `pyVmomi.pbm.ServiceInstanceContent` object provides
   access to the Storage Policy managed objects.
   """
   @property
   def content(self) -> ServiceInstanceContent:
      """Contains references to Storage Policy managed objects."""
      ...

   def RetrieveContent(self) -> ServiceInstanceContent:
      """
      Retrieves the properties of the Storage Policy service instance.
      
      Returns:
          Service instance properties that provide access to
          Storage Policy managed objects.
      """
      ...


class ServiceInstanceContent(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.ServiceInstanceContent` data object defines properties for the
   `pyVmomi.pbm.ServiceInstance` managed object.
   
   Attributes:
       aboutInfo: Contains information that identifies the Storage Policy service.
       sessionManager: For internal use.
       capabilityMetadataManager: For internal use.
       profileManager: Provides access to the Storage Policy ProfileManager.
       complianceManager: Provides access to the Storage Policy ComplianceManager.
       placementSolver: Provides access to the Storage Policy PlacementSolver.
       replicationManager: Provides access to the Storage Policy ReplicationManager.
   """
   aboutInfo: AboutInfo
   sessionManager: pyVmomi.pbm.auth.SessionManager
   capabilityMetadataManager: pyVmomi.pbm.capability.CapabilityMetadataManager
   profileManager: pyVmomi.pbm.profile.ProfileManager
   complianceManager: pyVmomi.pbm.compliance.ComplianceManager
   placementSolver: pyVmomi.pbm.placement.PlacementSolver
   replicationManager: _typing.Optional[pyVmomi.pbm.replication.ReplicationManager] = None
