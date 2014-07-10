.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../../vim/Task.rst

.. _vim.HostSystem: ../../../vim/HostSystem.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.ResourcePool: ../../../vim/ResourcePool.rst

.. _vim.VirtualMachine: ../../../vim/VirtualMachine.rst

.. _vim.vm.check.Result: ../../../vim/vm/check/Result.rst

.. _vim.fault.InvalidState: ../../../vim/fault/InvalidState.rst

.. _vmodl.fault.InvalidArgument: ../../../vmodl/fault/InvalidArgument.rst

.. _vim.fault.NoActiveHostInCluster: ../../../vim/fault/NoActiveHostInCluster.rst


vim.vm.check.CompatibilityChecker
=================================
  A singleton managed object that can answer questions about compatibility of a virtual machine with a host.


:since: `vSphere API 4.0`_


Attributes
----------


Methods
-------


CheckCompatibility(vm, host, pool, testType):
   Tests whether or not a virtual machine could be placed on the given host in the given resource pool.


  Privilege:
               System.View



  Args:
    vm (`vim.VirtualMachine`_):
       The virtual machine we'd like to place.


    host (`vim.HostSystem`_, optional):
       The host we would like the virtual machine to execute on. The host parameter may be left unset if the compute resource associated with the pool represents a stand-alone host or a DRS-enabled cluster. In the former case the stand-alone host is used. In the latter case, each connected host in the cluster that is not in maintenance mode is tested. If the virtual machine is a template then either this parameter or the pool parameter must be set.


    pool (`vim.ResourcePool`_, optional):
       The resource pool we would like the virtual machine to reside in. If the pool parameter is left unset, then the virtual machine's current pool is assumed. If the virtual machine is a template then either this parameter or the host parameter must be set.


    testType (`str`_, optional):
       The set of tests to run. If this argument is not set, all tests will be run. See `CheckTestType`_ for possible values.




  Returns:
     `vim.Task`_:
         The potential problems associated with placing this virtual machine in the proposed location. If multiple hosts are tested against a `CheckResult`_ is returned for each host.

  Raises:

    `vim.fault.InvalidState`_: 
       vim.fault.InvalidState

    `vim.fault.NoActiveHostInCluster`_: 
       vim.fault.NoActiveHostInCluster

    `vmodl.fault.InvalidArgument`_: 
       if the desired host and pool are not associated with the same compute resource, or if the host parameter is left unset when the specified pool is ssociated with a non-DRS cluster.


