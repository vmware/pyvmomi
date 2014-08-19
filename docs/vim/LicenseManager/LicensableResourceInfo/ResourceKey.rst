vim.LicenseManager.LicensableResourceInfo.ResourceKey
=====================================================
  Identifiers of currently supported resources.
  :contained by: `vim.LicenseManager.LicensableResourceInfo <vim/LicenseManager/LicensableResourceInfo.rst>`_

  :type: `vim.LicenseManager.LicensableResourceInfo.ResourceKey <vim/LicenseManager/LicensableResourceInfo/ResourceKey.rst>`_

  :name: numVmsStarting

values:
--------

memoryForVms
   Total size of memory configured for VMs on this host, measured in kilobytes.

memorySize
   Total size of memory installed on this host, measured in kilobytes.

numVmsStarted
   Number of VMs already running on this host.

numCpuPackages
   Number of CPU packages on this host.

numVmsStarting
   Number of VMs that are currently powering-on, immigrating, etc.

numCpuCores
   Number of licensable CPU cores/compute-units on this host.
