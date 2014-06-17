.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.cluster.DasAdmissionControlInfo: ../../vim/cluster/DasAdmissionControlInfo.rst


vim.cluster.FailoverLevelAdmissionControlInfo
=============================================
  The current admission control related information if the cluster was configured with a FailoverLevelAdmissionControlPolicy.
:extends: vim.cluster.DasAdmissionControlInfo_
:since: `vSphere API 4.0`_

Attributes:
    currentFailoverLevel (`int`_):

       Current failover level. This is the number of physical host failures that can be tolerated without impacting the ability to satisfy the minimums for all running virtual machines. This represents the current value, as opposed to desired value configured by the user.
