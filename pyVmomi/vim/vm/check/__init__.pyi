# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.vm



class CompatibilityChecker(pyVmomi.VmomiSupport.ManagedObject):
   def CheckCompatibility(self, vm: pyVmomi.vim.VirtualMachine, host: _typing.Optional[pyVmomi.vim.HostSystem], pool: _typing.Optional[pyVmomi.vim.ResourcePool], testType: list[str]) -> pyVmomi.vim.Task: ...
   def CheckVmConfig(self, spec: pyVmomi.vim.vm.ConfigSpec, vm: _typing.Optional[pyVmomi.vim.VirtualMachine], host: _typing.Optional[pyVmomi.vim.HostSystem], pool: _typing.Optional[pyVmomi.vim.ResourcePool], testType: list[str]) -> pyVmomi.vim.Task: ...
   def CheckPowerOn(self, vm: pyVmomi.vim.VirtualMachine, host: _typing.Optional[pyVmomi.vim.HostSystem], pool: _typing.Optional[pyVmomi.vim.ResourcePool], testType: list[str]) -> pyVmomi.vim.Task: ...


class ProvisioningChecker(pyVmomi.VmomiSupport.ManagedObject):
   def QueryVMotionCompatibilityEx(self, vm: list[pyVmomi.vim.VirtualMachine], host: list[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task: ...
   def CheckMigrate(self, vm: pyVmomi.vim.VirtualMachine, host: _typing.Optional[pyVmomi.vim.HostSystem], pool: _typing.Optional[pyVmomi.vim.ResourcePool], state: _typing.Optional[pyVmomi.vim.VirtualMachine.PowerState], testType: list[str]) -> pyVmomi.vim.Task: ...
   def CheckRelocate(self, vm: pyVmomi.vim.VirtualMachine, spec: pyVmomi.vim.vm.RelocateSpec, testType: list[str]) -> pyVmomi.vim.Task: ...
   def CheckClone(self, vm: pyVmomi.vim.VirtualMachine, folder: pyVmomi.vim.Folder, name: str, spec: pyVmomi.vim.vm.CloneSpec, testType: list[str]) -> pyVmomi.vim.Task: ...
   def CheckInstantClone(self, vm: pyVmomi.vim.VirtualMachine, spec: pyVmomi.vim.vm.InstantCloneSpec, testType: list[str]) -> pyVmomi.vim.Task: ...


class Result(pyVmomi.vmodl.DynamicData):
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   warning: list[pyVmomi.vmodl.MethodFault] = []
   error: list[pyVmomi.vmodl.MethodFault] = []

class TestType:
   pass
