.. _vim.ServiceInstance: ../../vim/ServiceInstance.rst

.. _vim.ServiceInstance.ValidateMigrationTestType: ../../vim/ServiceInstance/ValidateMigrationTestType.rst

vim.ServiceInstance.ValidateMigrationTestType
=============================================
  Types of tests available for validateMigration.
  :contained by: `vim.ServiceInstance`_

  :type: `vim.ServiceInstance.ValidateMigrationTestType`_

  :name: resourceTests

values:
--------

resourceTests
   Tests that check that the destination resource pool can support the virtual machine if it is powered on. The destination host or cluster is relevant because it will affect the amount of overhead memory required to run the virtual machine.

sourceTests
   Tests that examine only the configuration of the virtual machine and its current host; the destination resource pool and host or cluster are irrelevant.

diskAccessibilityTests
   Tests that check that the destination host or cluster can see the datastores where the virtual machine's virtual disks are currently located. The destination resource pool is irrelevant. If you are planning to relocate the virtual disks, do not use these tests; instead examine the relevant datastore objects for your planned disk locations to see if they are accessible to the destination host.

compatibilityTests
   Tests that examine both the virtual machine and the destination host or cluster; the destination resource pool is irrelevant. This set excludes tests that fall into the diskAccessibilityTests group.
