# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.vm



class CompatibilityChecker(pyVmomi.VmomiSupport.ManagedObject):
   """
   A singleton managed object that can answer questions about compatibility
   of a virtual machine with a host.
   """
   def CheckCompatibility(self, vm: pyVmomi.vim.VirtualMachine, host: _typing.Optional[pyVmomi.vim.HostSystem], pool: _typing.Optional[pyVmomi.vim.ResourcePool], testType: list[str]) -> pyVmomi.vim.Task:
      """
      Tests whether or not a virtual machine could be placed on
      the given host in the given resource pool.
      
      Args:
          vm: The virtual machine we'd like to place.
          host: The host we would like the virtual machine
              to execute on. The host parameter may be left unset if the compute
              resource associated with the pool represents a stand-alone host
              or a DRS-enabled cluster. In the former case the stand-alone host is
              used. In the latter case, each connected host in the cluster
              that is not in maintenance mode is tested. If the virtual machine is a
              template then either this parameter or the pool parameter must be set.
          pool: The resource pool we would like the virtual machine
              to reside in. If the pool parameter is left unset, then the virtual
              machine's current pool is assumed. If the virtual machine is a template
              then either this parameter or the host parameter must be set.
          testType: The set of tests to run. If this argument is not set, all
              tests will be run. See `pyVmomi.vim.vm.check.TestType` for possible values.
      
      Returns:
          The potential problems associated with placing this virtual
          machine in the proposed location.
          If multiple hosts are tested against a `pyVmomi.vim.vm.check.Result`
          is returned for each host.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              host or virtual machine's current state. For example, if the host
              is in maintenance mode or if the virtual machine's configuration
              information is not available.
          pyVmomi.vmodl.fault.InvalidArgument: if the desired host and pool are not associated
              with the same compute resource, the host parameter is left unset
              when the specified pool is associated with a non-DRS cluster, or
              if the specified vm does not exist.
          pyVmomi.vim.fault.DatacenterMismatch: if the provided host and pool do not belong
              to the same datacenter.
      """
      ...
   def CheckVmConfig(self, spec: pyVmomi.vim.vm.ConfigSpec, vm: _typing.Optional[pyVmomi.vim.VirtualMachine], host: _typing.Optional[pyVmomi.vim.HostSystem], pool: _typing.Optional[pyVmomi.vim.ResourcePool], testType: list[str]) -> pyVmomi.vim.Task:
      """
      Tests whether the provided virtual machine specification can be applied
      on the given host and resource pool.
      
      Args:
          spec: The specification of the virtual machine to create.
              Note that `spec.skipExtensionCompatibilityChecks` is ignored.
          vm: The existing virtual machine to apply the spec to.
              If this is not provided, the spec is assumed to be for the creation
              of a new virtual machine.
          host: The host we would like the virtual machine
              to execute on. The host parameter may be left unset if the compute
              resource associated with the pool represents a stand-alone host
              or a DRS-enabled cluster. In the former case the stand-alone host
              is used. In the latter case, each connected host in the cluster
              that is not in maintenance mode is tested. If the virtual machine
              is a template, then either this parameter or the pool parameter
              must be set.
          pool: The resource pool we would like the virtual machine
              to reside in. If the pool parameter is left unset, then we use the
              host's root resource pool.
          testType: The set of tests to run. If this argument is not set, all
              tests will be run. See `pyVmomi.vim.vm.check.TestType` for possible values.
      
      Returns:
          The potential problems associated with placing this virtual
          machine in the proposed location.
          If multiple hosts are tested against a `pyVmomi.vim.vm.check.Result`
          is returned for each host.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the desired host and pool are not associated
              with the same compute resource, the host parameter is left unset
              when the specified pool is associated with a non-DRS cluster, or
              if the provided vm does not exist.
          pyVmomi.vim.fault.DatacenterMismatch: if the provided host and pool do not belong
              to the same datacenter.
      """
      ...
   def CheckPowerOn(self, vm: pyVmomi.vim.VirtualMachine, host: _typing.Optional[pyVmomi.vim.HostSystem], pool: _typing.Optional[pyVmomi.vim.ResourcePool], testType: list[str]) -> pyVmomi.vim.Task:
      """
      Tests whether the provided virtual machine can be powered on
      on the given host and/or resource pool.
      
      Args:
          vm: The virtual machine to power on.
          host: The host on which we want to power on the virtual machine.
              The host parameter may be left unset if the compute
              resource associated with the pool represents a stand-alone host
              or a DRS-enabled cluster. In the former case the stand-alone host
              is used. In the latter case, each connected host in the cluster
              that is not in maintenance mode is tested. Either this parameter
              or the pool parameter must be set.
          pool: The resource pool we would like the virtual machine to run
              in. If the pool parameter is left unset, we use the host's
              root resource pool.
          testType: The set of tests to run. If this argument is not set,
              all tests will be run. See `pyVmomi.vim.vm.check.TestType` for possible values.
      
      Returns:
          The potential problems associated with powering on this virtual
          machine at the proposed location.
          If multiple hosts are tested, a `pyVmomi.vim.vm.check.Result`
          is returned for each host.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the desired host and pool are not associated
              with the same compute resource, the host parameter is left unset
              when the specified pool is associated with a non-DRS cluster, or
              if the provided vm does not exist.
          pyVmomi.vim.fault.DatacenterMismatch: if the provided host and pool do not belong
              to the same datacenter.
      """
      ...


class ProvisioningChecker(pyVmomi.VmomiSupport.ManagedObject):
   """
   A singleton managed object that can answer questions about
   the feasibility of certain provisioning operations.
   """
   def QueryVMotionCompatibilityEx(self, vm: list[pyVmomi.vim.VirtualMachine], host: list[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task:
      """
      Investigates the general VMotion compatibility of a set of virtual machines
      with a set of hosts.
      
      The virtual machine may be in any power state. Hosts
      may be in any connection state and also may be in maintenance mode.
      
      Args:
          vm: The set of virtual machines to analyze for compatibility. All
              virtual machines are assumed to be powered-on for the purposes of
              this operation.
          host: The set of hosts to analyze for compatibility. All hosts
              are assumed to be connected and not in maintenance mode for the
              purposes of this operation.
      
      Returns:
          The problems associated with these potential VMotions.
          A `pyVmomi.vim.vm.check.Result` is returned for each vm/host
          combination. In case a VM or a host is not found, returned result
          will contain an error \"Managed Object Not Found\" for the missing
          host or VM.
      """
      ...
   def CheckMigrate(self, vm: pyVmomi.vim.VirtualMachine, host: _typing.Optional[pyVmomi.vim.HostSystem], pool: _typing.Optional[pyVmomi.vim.ResourcePool], state: _typing.Optional[pyVmomi.vim.VirtualMachine.PowerState], testType: list[str]) -> pyVmomi.vim.Task:
      """
      Tests the feasibility of a proposed
      `pyVmomi.vim.VirtualMachine.migrate` operation.
      
      Args:
          vm: The virtual machine we propose to migrate.
          host: The target host on which the virtual machines will run. The host
              parameter may be left unset if the compute resource associated with
              the target pool represents a stand-alone host or a DRS-enabled
              cluster. In the former case the stand-alone host is used as the
              target host. In the latter case, each connected host in the cluster
              that is not in maintenance mode is tested as a target host.
              If the virtual machine is a template then either this
              parameter or the pool parameter must be set.
          pool: The target resource pool for the virtual machines. If the
              pool parameter is left unset, the target pool for each particular
              virtual machine's migration will be that virtual machine's current
              pool. If the virtual machine is a template then either this
              parameter or the host parameter must be set.
              The pool parameter must be set for testing the feasibility of
              migration to a different datacenter or different vCenter service.
          state: The power state that the virtual machines must have. If
              this argument is not set, each virtual machine is evaluated
              according to its current power state.
          testType: The set of tests to run. If this argument is not set, all
              tests will be run. See `pyVmomi.vim.vm.check.TestType` for possible values.
      
      Returns:
          The problems associated with this potential migrate.
          If multiple hosts are tested against a `pyVmomi.vim.vm.check.Result`
          is returned for each host.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: An InvalidState fault is thrown if the
              operation failed due to the current state of the system.
      """
      ...
   def CheckRelocate(self, vm: pyVmomi.vim.VirtualMachine, spec: pyVmomi.vim.vm.RelocateSpec, testType: list[str]) -> pyVmomi.vim.Task:
      """
      Tests the feasibility of a proposed
      `pyVmomi.vim.VirtualMachine.relocate` operation.
      
      Args:
          vm: The virtual machine we propose to relocate.
          spec: The specification of where to relocate the virtual machine.
              In cases where DRS would automatically select a host, all potential
              hosts are tested against.
              The host parameter in the spec may be left unset for checking
              feasibility of relocation to a different datacenter or different
              vCenter service, if the compute resource associated with the
              target pool represents a stand-alone host, the host is tested
              against, otherwise each connected host in the cluster that is
              not in maintenance mode represented by the target pool is tested
              as a target host.
              Note that `spec.skipExtensionCompatibilityChecks` is ignored.
          testType: The set of tests to run. If this argument is not set, all
              tests will be run. See `pyVmomi.vim.vm.check.TestType` for possible values.
      
      Returns:
          The problems associated with this potential relocate.
          If multiple hosts are tested against a `pyVmomi.vim.vm.check.Result`
          is returned for each host.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              host or virtual machine's current state. For example, if the host is in
              maintenance mode, or if the virtual machine's configuration information
              is not available.
      """
      ...
   def CheckClone(self, vm: pyVmomi.vim.VirtualMachine, folder: pyVmomi.vim.Folder, name: str, spec: pyVmomi.vim.vm.CloneSpec, testType: list[str]) -> pyVmomi.vim.Task:
      """
      Tests the feasibility of a proposed
      `pyVmomi.vim.VirtualMachine.clone` operation.
      
      Args:
          vm: The virtual machine we propose to clone.
          folder: The location of the new virtual machine.
          name: The name of the new virtual machine.
          spec: Specifies how to clone the virtual machine. In cases
              where DRS would automatically select a host, all potential
              hosts are tested against.
          testType: The set of tests to run. If this argument is not set, all
              tests will be run. See `pyVmomi.vim.vm.check.TestType` for possible values.
      
      Returns:
          The problems associated with this potential clone.
          If multiple hosts are tested against a `pyVmomi.vim.vm.check.Result`
          is returned for each host.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state. For example, if the virtual machine
              configuration information is not available.
      """
      ...
   def CheckInstantClone(self, vm: pyVmomi.vim.VirtualMachine, spec: pyVmomi.vim.vm.InstantCloneSpec, testType: list[str]) -> pyVmomi.vim.Task:
      """
      Tests the feasibility of a proposed
      `pyVmomi.vim.VirtualMachine.instantClone` operation.
      
      Args:
          vm: The virtual machine we propose to instant clone.
          spec: Specifies how to instant clone the virtual machine.
          testType: The set of tests to run. If this argument is not set, all
              tests will be run. See `pyVmomi.vim.vm.check.TestType` for possible values.
      
      Returns:
          The problems associated with this potential instant clone.
          If multiple hosts are tested against a `pyVmomi.vim.vm.check.Result`
          is returned for each host.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state. For example, if the virtual
              machine configuration information is not available.
      """
      ...


class Result(pyVmomi.vmodl.DynamicData):
   """
   The result of a call to any of the methods in either
   `pyVmomi.vim.vm.check.CompatibilityChecker` or `pyVmomi.vim.vm.check.ProvisioningChecker`.
   
   Attributes:
       vm: The virtual machine involved in the testing.
       host: The host involved in the testing.
       warning: A list of faults representing problems which may
           require attention, but which are not fatal.
       error: A list of faults representing problems which are fatal
           to the operation.
           
           For `pyVmomi.vim.vm.check.ProvisioningChecker` an error means that the
           given provisioning operation would fail.
           For `pyVmomi.vim.vm.check.CompatibilityChecker` an error means that either
           a power-on of this virtual machine would fail, or that the
           virtual machine would not run correctly once powered-on.
   """
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   warning: list[pyVmomi.vmodl.MethodFault] = []
   error: list[pyVmomi.vmodl.MethodFault] = []

class TestType:
   """
   The types of tests which can requested by any of the methods in either
   `pyVmomi.vim.vm.check.CompatibilityChecker` or `pyVmomi.vim.vm.check.ProvisioningChecker`.
   
   Only `extensionTests` evaluates extension-registered compatibility
   constraints, even if a constraint conceptually belongs to another test type. For
   example, a constraint whose `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.ConstraintType`
   is `POOL` is not evaluated as part of `resourcePoolTests`; it is only
   evaluated when `extensionTests` is included.
   
   `extensionTests`, in turn, is not scoped to a single domain: requesting it
   evaluates every constraint registered on the virtual machine, regardless of
   `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.ConstraintType`. So there is no way
   to request \"the complete, resource-pool-only picture\" for a virtual machine with
   both a `POOL` constraint and, say, a `DEVICE` constraint: requesting
   only `resourcePoolTests` omits the `POOL` constraint, while adding
   `extensionTests` to also cover it pulls in the unrelated `DEVICE`
   constraint as well. The same applies to any other test type.
   """
   pass
