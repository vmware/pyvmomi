.. _vim.Network: ../../../vim/Network.rst

.. _vim.Datastore: ../../../vim/Datastore.rst

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.EsxAgentHostManager.ConfigInfo
=======================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    agentVmDatastore (`vim.Datastore`_, optional):

       Datastore used for deploying Agent VMs on this host.
    agentVmNetwork (`vim.Network`_, optional):

       Management Network for Agent VMs on this host.
