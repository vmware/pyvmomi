.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../../vim/Task.rst

.. _vim.HostSystem: ../../../vim/HostSystem.rst

.. _MigrateVM_Task: ../../../vim/VirtualMachine.rst#migrate

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _RelocateVM_Task: ../../../vim/VirtualMachine.rst#relocate

.. _vim.ResourcePool: ../../../vim/ResourcePool.rst

.. _vim.VirtualMachine: ../../../vim/VirtualMachine.rst

.. _vim.vm.RelocateSpec: ../../../vim/vm/RelocateSpec.rst

.. _vim.vm.check.Result: ../../../vim/vm/check/Result.rst

.. _vim.fault.InvalidState: ../../../vim/fault/InvalidState.rst

.. _vmodl.fault.NotSupported: ../../../vmodl/fault/NotSupported.rst

.. _vmodl.fault.InvalidArgument: ../../../vmodl/fault/InvalidArgument.rst

.. _vim.fault.InvalidPowerState: ../../../vim/fault/InvalidPowerState.rst

.. _vim.VirtualMachine.PowerState: ../../../vim/VirtualMachine/PowerState.rst


vim.vm.check.ProvisioningChecker
================================
  A singleton managed object that can answer questions about the feasibility of certain provisioning operations.


:since: `vSphere API 4.0`_


Attributes
----------


Methods
-------


QueryVMotionCompatibilityEx(vm, host):
   Investigates the general VMotion compatibility of a set of virtual machines with a set of hosts. The virtual machine may be in any power state. Hosts may be in any connection state and also may be in maintenance mode.


  Privilege:
               System.View



  Args:
    vm (`vim.VirtualMachine`_):
       The set of virtual machines to analyze for compatibility. All virtual machines are assumed to be powered-on for the purposes of this operation.


    host (`vim.HostSystem`_):
       The set of hosts to analyze for compatibility. All hosts are assumed to be connected and not in maintenance mode for the purposes of this operation.




  Returns:
     `vim.Task`_:
         The problems associated with these potential VMotions. A `CheckResult`_ is returned for each vm/host combination.


CheckMigrate(vm, host, pool, state, testType):
   Tests the feasibility of a proposed `MigrateVM_Task`_ operation.


  Privilege:
               System.View



  Args:
    vm (`vim.VirtualMachine`_):
       The virtual machine we propose to migrate.


    host (`vim.HostSystem`_, optional):
       The target host on which the virtual machines will run. The host parameter may be left unset if the compute resource associated with the target pool represents a stand-alone host or a DRS-enabled cluster. In the former case the stand-alone host is used as the target host. In the latter case, each connected host in the cluster that is not in maintenance mode is tested as a target host. If the virtual machine is a template then either this parameter or the pool parameter must be set.


    pool (`vim.ResourcePool`_, optional):
       The target resource pool for the virtual machines. If the pool parameter is left unset, the target pool for each particular virtual machine's migration will be that virtual machine's current pool. If the virtual machine is a template then either this parameter or the host parameter must be set.


    state (`vim.VirtualMachine.PowerState`_, optional):
       The power state that the virtual machines must have. If this argument is not set, each virtual machine is evaluated according to its current power state.


    testType (`str`_, optional):
       The set of tests to run. If this argument is not set, all tests will be run.




  Returns:
     `vim.Task`_:
         The problems associated with this potential migrate. If multiple hosts are tested against a `CheckResult`_ is returned for each host.

  Raises:

    `vim.fault.InvalidState`_:
       vim.fault.InvalidState

    `vmodl.fault.InvalidArgument`_:
       if the target host(s) and target pool for a migration are not associated with the same compute resource, or if the host parameter is left unset when the target pool is associated with a non-DRS cluster.

    `vim.fault.InvalidPowerState`_:
       if the state argument is set and at least one of the specified virtual machines is not in that power state.


CheckRelocate(vm, spec, testType):
   Tests the feasibility of a proposed `RelocateVM_Task`_ operation.


  Privilege:
               System.View



  Args:
    vm (`vim.VirtualMachine`_):
       The virtual machine we propose to relocate.


    spec (`vim.vm.RelocateSpec`_):
       The specification of where to relocate the virtual machine. In cases where DRS would automatically select a host, all potential hosts are tested against.


    testType (`str`_, optional):




  Returns:
     `vim.Task`_:
         The problems associated with this potential relocate. If multiple hosts are tested against a `CheckResult`_ is returned for each host.

  Raises:

    `vim.fault.InvalidState`_:
       if the operation cannot be performed because of the host or virtual machine's current state. For example, if the host is in maintenance mode, or if the virtual machine's configuration information is not available.

    `vmodl.fault.NotSupported`_:
       if the virtual machine is marked as a template.

    `vmodl.fault.InvalidArgument`_:
       in the following cases:
        * the target host and target pool are not associated with the same compute resource
        * the target pool represents a cluster without DRS enabled, and the host is not specified
        * Datastore in a diskLocator entry is not specified
        * the specified device ID cannot be found in the virtual machine's current configuration
        * the object specified in relocate cannot be found
