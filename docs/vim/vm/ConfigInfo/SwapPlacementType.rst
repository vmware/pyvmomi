.. _swapPlacement: ../../../vim/vm/ConfigInfo.rst#swapPlacement

.. _vmSwapPlacement: ../../../vim/ComputeResource/ConfigInfo.rst#vmSwapPlacement

.. _vim.vm.ConfigInfo: ../../../vim/vm/ConfigInfo.rst

.. _localSwapDatastore: ../../../vim/host/ConfigInfo.rst#localSwapDatastore

.. _vim.vm.ConfigInfo.SwapPlacementType: ../../../vim/vm/ConfigInfo/SwapPlacementType.rst

vim.vm.ConfigInfo.SwapPlacementType
===================================
  Available choices for virtual machine swapfile placement policy. This is the set of legal values for the virtual machine configuration's `swapPlacement`_ property. All values except for "inherit" and "vmConfigured" are also valid values for a compute resource configuration's `vmSwapPlacement`_ property.
  :contained by: `vim.vm.ConfigInfo`_

  :type: `vim.vm.ConfigInfo.SwapPlacementType`_

  :name: hostLocal

values:
--------

hostLocal
   Store the swapfile in the datastore specified by the `localSwapDatastore`_ property of the virtual machine's host, if that property is set and indicates a datastore with sufficient free space. Otherwise store the swapfile in the same directory as the virtual machine.Note: This setting may degrade VMotion performance.

vmDirectory
   Store the swapfile in the same directory as the virtual machine.

inherit
   Honor the virtual machine swapfile placement policy of the compute resource that contains this virtual machine.
