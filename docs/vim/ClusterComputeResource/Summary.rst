
vim.ClusterComputeResource.Summary
==================================
  The `ClusterComputeResourceSummary <vim/ClusterComputeResource/Summary.rst>`_ data object encapsulates runtime properties of a `ClusterComputeResource <vim/ClusterComputeResource.rst>`_ .
:extends: vim.ComputeResource.Summary_

Attributes:
    currentFailoverLevel (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Current failover level. This is the number of physical host failures that can be tolerated without impacting the ability to satisfy the minimums for all running virtual machines. This represents the current value, as opposed to desired value configured by the user.
    admissionControlInfo (`vim.cluster.DasAdmissionControlInfo <vim/cluster/DasAdmissionControlInfo.rst>`_, optional):

       Information about the current amount of resources available for a vSphere HA cluster. The actual type of admissionControlInfo will depend on what kind of `ClusterDasAdmissionControlPolicy <vim/cluster/DasAdmissionControlPolicy.rst>`_ was used to configure the cluster.
    numVmotions (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Total number of migrations with VMotion that have been done internal to this cluster.
    targetBalance (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The target balance, in terms of standard deviation, for a DRS cluster. Units are thousandths. For example, 12 represents 0.012.
    currentBalance (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The current balance, in terms of standard deviation, for a DRS cluster. Units are thousandths. For example, 12 represents 0.012.
    currentEVCModeKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The Enhanced VMotion Compatibility mode that is currently in effect for all hosts in this cluster; unset if no EVC mode is active.See `supportedEVCMode <vim/Capability.rst#supportedEVCMode>`_ 
    dasData (`vim.cluster.DasData <vim/cluster/DasData.rst>`_, optional):

       Data pertaining to DAS.
