
vim.StorageResourceManager.PodStorageDrsEntry
=============================================
  An entry containing storage DRS configuration, runtime results, and history for a pod `StoragePod <vim/StoragePod.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    storageDrsConfig (`vim.storageDrs.ConfigInfo <vim/storageDrs/ConfigInfo.rst>`_):

       Storage DRS configuration.
    recommendation ([`vim.cluster.Recommendation <vim/cluster/Recommendation.rst>`_], optional):

       List of recommended actions for the Storage Pod. It is possible that the current set of recommendations may be empty, either due to not having any running dynamic recommendation generation module, or since there may be no recommended actions at this time.
    drsFault ([`vim.cluster.DrsFaults <vim/cluster/DrsFaults.rst>`_], optional):

       A collection of the DRS faults generated in the last Storage DRS invocation. Each element of the collection is the set of faults generated in one recommendation.
    actionHistory ([`vim.cluster.ActionHistory <vim/cluster/ActionHistory.rst>`_], optional):

       The set of actions that have been performed recently.
