
vim.cluster.EnterMaintenanceResult
==================================
  EnterMaintenanceResult is the base class of the result returned to the `ClusterEnterMaintenanceMode <vim/ClusterComputeResource.rst#enterMaintenanceMode>`_ method.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    recommendations ([`vim.cluster.Recommendation <vim/cluster/Recommendation.rst>`_], optional):

       The list of recommendations for hosts that Virtual Center will be able to evacuate. Each recommendation consists of a host maintenance action `ClusterAction <vim/cluster/Action.rst>`_ for a host, along with zero or more vmotions for evacuation. Application of the recommendations is not supported currently. The client will have to put the hosts into maintenance mode by calling the separate method `EnterMaintenanceMode_Task <vim/HostSystem.rst#enterMaintenanceMode>`_ .
    fault (`vim.cluster.DrsFaults <vim/cluster/DrsFaults.rst>`_, optional):

       The faults that explain why the Virtual Center cannot evacuate some hosts.
