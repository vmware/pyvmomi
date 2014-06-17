.. _vim.vApp.IPAssignmentInfo: ../../../vim/vApp/IPAssignmentInfo.rst

.. _vim.vApp.IPAssignmentInfo.IpAllocationPolicy: ../../../vim/vApp/IPAssignmentInfo/IpAllocationPolicy.rst

vim.vApp.IPAssignmentInfo.IpAllocationPolicy
============================================
  IP allocation policy for a deployment.
  :contained by: `vim.vApp.IPAssignmentInfo`_

  :type: `vim.vApp.IPAssignmentInfo.IpAllocationPolicy`_

  :name: fixedAllocatedPolicy

values:
--------

dhcpPolicy
   Specifies that DHCP must be used to allocate IP addresses to the vApp

fixedPolicy
   Specifies that IP addresses are configured manually when the vApp is deployed and will be kept until reconfigured or the vApp destroyed. This will ensure that a vApp gets a consistent IP for its life-time.

fixedAllocatedPolicy
   Specifies that IP allocation is done through the range managed by the VI platform. The IP addresses are allocated at first power-on, and remain allocated at power-off. This will ensure that a vApp gets a consistent IP for its life-time.

transientPolicy
   Specifies that IP allocation is done through the range managed by the vSphere platform. The IP addresses are allocated when needed, typically at power-on, and deallocated during power-off. There is no guarantee that a vApp will get the same IP address when restarted.
