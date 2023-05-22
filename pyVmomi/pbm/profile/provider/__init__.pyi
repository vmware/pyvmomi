from pyVmomi import vmodl
from pyVmomi.VmomiSupport import long


class DatastoreSpaceStatistics(vmodl.DynamicData):
    @property
    def profileId(self) -> str: ...
    @profileId.setter
    def profileId(self, value: str):
        self._profileId = value
    @property
    def physicalTotalInMB(self) -> long: ...
    @physicalTotalInMB.setter
    def physicalTotalInMB(self, value: long):
        self._physicalTotalInMB = value
    @property
    def physicalFreeInMB(self) -> long: ...
    @physicalFreeInMB.setter
    def physicalFreeInMB(self, value: long):
        self._physicalFreeInMB = value
    @property
    def physicalUsedInMB(self) -> long: ...
    @physicalUsedInMB.setter
    def physicalUsedInMB(self, value: long):
        self._physicalUsedInMB = value
    @property
    def logicalLimitInMB(self) -> long: ...
    @logicalLimitInMB.setter
    def logicalLimitInMB(self, value: long):
        self._logicalLimitInMB = value
    @property
    def logicalFreeInMB(self) -> long: ...
    @logicalFreeInMB.setter
    def logicalFreeInMB(self, value: long):
        self._logicalFreeInMB = value
    @property
    def logicalUsedInMB(self) -> long: ...
    @logicalUsedInMB.setter
    def logicalUsedInMB(self, value: long):
        self._logicalUsedInMB = value