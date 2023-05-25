from typing import List, Literal
from pyVmomi import vim, vmodl
from pyVmomi.VmomiSupport import ManagedObject


class CompatibilityChecker(ManagedObject):
    def CheckCompatibility(self, vm: vim.VirtualMachine, host: vim.HostSystem, pool: vim.ResourcePool, testType: List[str]) -> vim.Task: ...
    def CheckVmConfig(self, spec: vim.vm.ConfigSpec, vm: vim.VirtualMachine, host: vim.HostSystem, pool: vim.ResourcePool, testType: List[str]) -> vim.Task: ...
    def CheckPowerOn(self, vm: vim.VirtualMachine, host: vim.HostSystem, pool: vim.ResourcePool, testType: List[str]) -> vim.Task: ...


class ProvisioningChecker(ManagedObject):
    def QueryVMotionCompatibilityEx(self, vm: List[vim.VirtualMachine], host: List[vim.HostSystem]) -> vim.Task: ...
    def CheckMigrate(self, vm: vim.VirtualMachine, host: vim.HostSystem, pool: vim.ResourcePool, state: vim.VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended'], testType: List[str]) -> vim.Task: ...
    def CheckRelocate(self, vm: vim.VirtualMachine, spec: vim.vm.RelocateSpec, testType: List[str]) -> vim.Task: ...
    def CheckClone(self, vm: vim.VirtualMachine, folder: vim.Folder, name: str, spec: vim.vm.CloneSpec, testType: List[str]) -> vim.Task: ...
    def CheckInstantClone(self, vm: vim.VirtualMachine, spec: vim.vm.InstantCloneSpec, testType: List[str]) -> vim.Task: ...


class Result(vmodl.DynamicData):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def warning(self) -> List[vmodl.MethodFault]: ...
    @warning.setter
    def warning(self, value: List[vmodl.MethodFault]):
        self._warning = value
    @property
    def error(self) -> List[vmodl.MethodFault]: ...
    @error.setter
    def error(self, value: List[vmodl.MethodFault]):
        self._error = value