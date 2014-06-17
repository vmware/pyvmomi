.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _ClusterSlotPolicy: ../../vim/cluster/SlotPolicy.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.cluster.SlotPolicy
======================
  The base class `ClusterSlotPolicy`_ is used for specifying how the slot size is to be computed for the failover level HA admission control policy. By default, vSphere HA defines the slot size using the largest memory and cpu reservations of any powered on virtual machine in the cluster. Subclasses of this class define various policies to modify how the slot size is chosen to prevent outlier virtual machines (i.e. those with much larger reservations than the average) from skewing the slot size. If such a policy is chosen, outlier virtual machines will use multiple slots. Using such a policy introduces a risk that vSphere HA will be unable to failover these virtual machines because of resource fragmentation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
