from typing import List
from enum import Enum
from pyVmomi import pbm, vmodl
from pyVmomi.VmomiSupport import ManagedObject
from . import auth as auth
from . import capability as capability
from . import compliance as compliance
from . import fault as fault
from . import placement as placement
from . import profile as profile
from . import provider as provider
from . import replication as replication


class ServiceInstance(ManagedObject):
    @property
    def content(self) -> ServiceInstanceContent: ...
    def RetrieveContent(self) -> ServiceInstanceContent: ...


class AboutInfo(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value


class ExtendedElementDescription(vmodl.DynamicData):
    @property
    def label(self) -> str: ...
    @label.setter
    def label(self, value: str):
        self._label = value
    @property
    def summary(self) -> str: ...
    @summary.setter
    def summary(self, value: str):
        self._summary = value
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def messageCatalogKeyPrefix(self) -> str: ...
    @messageCatalogKeyPrefix.setter
    def messageCatalogKeyPrefix(self, value: str):
        self._messageCatalogKeyPrefix = value
    @property
    def messageArg(self) -> List[vmodl.KeyAnyValue]: ...
    @messageArg.setter
    def messageArg(self, value: List[vmodl.KeyAnyValue]):
        self._messageArg = value


class LoggingConfiguration(vmodl.DynamicData):
    @property
    def component(self) -> str: ...
    @component.setter
    def component(self, value: str):
        self._component = value
    @property
    def logLevel(self) -> str: ...
    @logLevel.setter
    def logLevel(self, value: str):
        self._logLevel = value


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
        INFO = "INFO"
        DEBUG = "DEBUG"
        TRACE = "TRACE"


class ServerObjectRef(vmodl.DynamicData):
    @property
    def objectType(self) -> str: ...
    @objectType.setter
    def objectType(self, value: str):
        self._objectType = value
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def serverUuid(self) -> str: ...
    @serverUuid.setter
    def serverUuid(self, value: str):
        self._serverUuid = value


    class ObjectType(Enum):
        virtualMachine = "virtualMachine"
        virtualMachineAndDisks = "virtualMachineAndDisks"
        virtualDiskId = "virtualDiskId"
        virtualDiskUUID = "virtualDiskUUID"
        datastore = "datastore"
        vsanObjectId = "vsanObjectId"
        fileShareId = "fileShareId"
        host = "host"
        cluster = "cluster"
        unknown = "unknown"


    class VvolType(Enum):
        Config = "Config"
        Data = "Data"
        Swap = "Swap"


class ServiceInstanceContent(vmodl.DynamicData):
    @property
    def aboutInfo(self) -> AboutInfo: ...
    @aboutInfo.setter
    def aboutInfo(self, value: AboutInfo):
        self._aboutInfo = value
    @property
    def sessionManager(self) -> pbm.auth.SessionManager: ...
    @sessionManager.setter
    def sessionManager(self, value: pbm.auth.SessionManager):
        self._sessionManager = value
    @property
    def capabilityMetadataManager(self) -> pbm.capability.CapabilityMetadataManager: ...
    @capabilityMetadataManager.setter
    def capabilityMetadataManager(self, value: pbm.capability.CapabilityMetadataManager):
        self._capabilityMetadataManager = value
    @property
    def profileManager(self) -> pbm.profile.ProfileManager: ...
    @profileManager.setter
    def profileManager(self, value: pbm.profile.ProfileManager):
        self._profileManager = value
    @property
    def complianceManager(self) -> pbm.compliance.ComplianceManager: ...
    @complianceManager.setter
    def complianceManager(self, value: pbm.compliance.ComplianceManager):
        self._complianceManager = value
    @property
    def placementSolver(self) -> pbm.placement.PlacementSolver: ...
    @placementSolver.setter
    def placementSolver(self, value: pbm.placement.PlacementSolver):
        self._placementSolver = value
    @property
    def replicationManager(self) -> pbm.replication.ReplicationManager: ...
    @replicationManager.setter
    def replicationManager(self, value: pbm.replication.ReplicationManager):
        self._replicationManager = value


class PbmDebugManager():


    class KeystoreName(Enum):
        SMS = "SMS"
        TRUSTED_ROOTS = "TRUSTED_ROOTS"