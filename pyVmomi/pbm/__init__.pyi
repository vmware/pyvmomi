from typing import List
from enum import Enum
from pyVmomi import vmodl
from pyVmomi.VmomiSupport import ManagedObject
from . import auth, capability, compliance, placement, profile, replication


class ServiceInstance(ManagedObject):
    @property
    def content(self) -> ServiceInstanceContent: ...
    def RetrieveContent(self) -> ServiceInstanceContent: ...


class AboutInfo(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @property
    def version(self) -> str: ...
    @property
    def instanceUuid(self) -> str: ...


class ExtendedElementDescription(vmodl.DynamicData):
    @property
    def label(self) -> str: ...
    @property
    def summary(self) -> str: ...
    @property
    def key(self) -> str: ...
    @property
    def messageCatalogKeyPrefix(self) -> str: ...
    @property
    def messageArg(self) -> List[vmodl.KeyAnyValue]: ...


class LoggingConfiguration(vmodl.DynamicData):
    @property
    def component(self) -> str: ...
    @property
    def logLevel(self) -> str: ...


    class Component(Enum):
        pbm = "pbm"
        vslm = "vslm"
        sms = "sms"
        spbm = "spbm"
        sps = "sps"
        httpclient_header = "httpclient_header"
        httpclient_content = "httpclient_content"
        vmomi = "vmomi"


    class LogLevel(Enum):
        INFO = "info"
        DEBUG = "debug"
        TRACE = "trace"


class ServerObjectRef(vmodl.DynamicData):
    @property
    def objectType(self) -> str: ...
    @property
    def key(self) -> str: ...
    @property
    def serverUuid(self) -> str: ...


    class ObjectType(Enum):
        virtualMachine = "virtualmachine"
        virtualMachineAndDisks = "virtualmachineanddisks"
        virtualDiskId = "virtualdiskid"
        virtualDiskUUID = "virtualdiskuuid"
        datastore = "datastore"
        vsanObjectId = "vsanobjectid"
        fileShareId = "fileshareid"
        host = "host"
        cluster = "cluster"
        unknown = "unknown"


    class VvolType(Enum):
        Config = "config"
        Data = "data"
        Swap = "swap"


class ServiceInstanceContent(vmodl.DynamicData):
    @property
    def aboutInfo(self) -> AboutInfo: ...
    @property
    def sessionManager(self) -> auth.SessionManager: ...
    @property
    def capabilityMetadataManager(self) -> capability.CapabilityMetadataManager: ...
    @property
    def profileManager(self) -> profile.ProfileManager: ...
    @property
    def complianceManager(self) -> compliance.ComplianceManager: ...
    @property
    def placementSolver(self) -> placement.PlacementSolver: ...
    @property
    def replicationManager(self) -> replication.ReplicationManager: ...


class PbmDebugManager():


    class KeystoreName(Enum):
        SMS = "sms"
        TRUSTED_ROOTS = "trusted_roots"