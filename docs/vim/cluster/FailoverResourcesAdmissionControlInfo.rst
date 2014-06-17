.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.cluster.DasAdmissionControlInfo: ../../vim/cluster/DasAdmissionControlInfo.rst


vim.cluster.FailoverResourcesAdmissionControlInfo
=================================================
  The current admission control related information if the cluster was configured with a FailoverResourcesAdmissionControlPolicy.
:extends: vim.cluster.DasAdmissionControlInfo_
:since: `vSphere API 4.0`_

Attributes:
    currentCpuFailoverResourcesPercent (`int`_):

       The percentage of cpu resources in the cluster available for failover.
    currentMemoryFailoverResourcesPercent (`int`_):

       The percentage of memory resources in the cluster available for failover.
