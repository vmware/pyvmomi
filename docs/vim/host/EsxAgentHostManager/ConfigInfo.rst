
vim.host.EsxAgentHostManager.ConfigInfo
=======================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    agentVmDatastore (`vim.Datastore <vim/Datastore.rst>`_, optional):

       Datastore used for deploying Agent VMs on this host.
    agentVmNetwork (`vim.Network <vim/Network.rst>`_, optional):

       Management Network for Agent VMs on this host.
