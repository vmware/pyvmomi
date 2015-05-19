.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _supportedEVCMode: ../../vim/Capability.rst#supportedEVCMode

.. _vim.cluster.DasData: ../../vim/cluster/DasData.rst

.. _ClusterComputeResource: ../../vim/ClusterComputeResource.rst

.. _vim.ComputeResource.Summary: ../../vim/ComputeResource/Summary.rst

.. _ClusterComputeResourceSummary: ../../vim/ClusterComputeResource/Summary.rst

.. _ClusterDasAdmissionControlPolicy: ../../vim/cluster/DasAdmissionControlPolicy.rst

.. _vim.cluster.DasAdmissionControlInfo: ../../vim/cluster/DasAdmissionControlInfo.rst


vim.ClusterComputeResource.Summary
==================================
  The `ClusterComputeResourceSummary`_ data object encapsulates runtime properties of a `ClusterComputeResource`_ .
:extends: vim.ComputeResource.Summary_

Attributes:
    currentFailoverLevel (`int`_):

       Current failover level. This is the number of physical host failures that can be tolerated without impacting the ability to satisfy the minimums for all running virtual machines. This represents the current value, as opposed to desired value configured by the user.
    admissionControlInfo (`vim.cluster.DasAdmissionControlInfo`_, optional):

       Information about the current amount of resources available for a vSphere HA cluster. The actual type of admissionControlInfo will depend on what kind of `ClusterDasAdmissionControlPolicy`_ was used to configure the cluster.
    numVmotions (`int`_):

       Total number of migrations with VMotion that have been done internal to this cluster.
    targetBalance (`int`_, optional):

       The target balance, in terms of standard deviation, for a DRS cluster. Units are thousandths. For example, 12 represents 0.012.
    currentBalance (`int`_, optional):

       The current balance, in terms of standard deviation, for a DRS cluster. Units are thousandths. For example, 12 represents 0.012.
    currentEVCModeKey (`str`_, optional):

       The Enhanced VMotion Compatibility mode that is currently in effect for all hosts in this cluster; unset if no EVC mode is active.See `supportedEVCMode`_ 
    dasData (`vim.cluster.DasData`_, optional):

       Data pertaining to DAS.
