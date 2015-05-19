.. _vim.cluster.DasVmConfigInfo: ../../../vim/cluster/DasVmConfigInfo.rst

.. _vim.cluster.DasVmConfigInfo.Priority: ../../../vim/cluster/DasVmConfigInfo/Priority.rst

vim.cluster.DasVmConfigInfo.Priority
====================================
  The priority of the virtual machine determines the preference given to it if sufficient capacity is not available to power on all failed virtual machines. For example, high priority virtual machines on a host get preference over low priority virtual machines.
  :contained by: `vim.cluster.DasVmConfigInfo`_

  :type: `vim.cluster.DasVmConfigInfo.Priority`_

  :name: high

values:
--------

disabled
   vSphere HA is disabled for this virtual machine.

high
   Virtual machines with this priority have a higher chance of powering on after a failure if there is insufficient capacity on hosts to meet all virtual machine needs.

medium
   Virtual machines with this priority have an intermediate chance of powering on after a failure if there is insufficient capacity on hosts to meet all virtual machine needs.

low
   Virtual machines with this priority have a lower chance of powering on after a failure if there is insufficient capacity on hosts to meet all virtual machine needs.
