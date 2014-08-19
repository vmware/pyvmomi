
vim.storageDrs.StoragePlacementResult
=====================================
  Both `RecommendDatastores <vim/StorageResourceManager.rst#recommendDatastores>`_ and `DatastoreEnterMaintenanceMode <vim/Datastore.rst#enterMaintenanceMode>`_ methods may invoke Storage DRS for recommendations on placing or evacuating virtual disks. StoragePlacementResult is the class of the result returned by the methods.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    recommendations ([`vim.cluster.Recommendation <vim/cluster/Recommendation.rst>`_], optional):

       The list of recommendations that the client needs to approve manually.
    drsFault (`vim.cluster.DrsFaults <vim/cluster/DrsFaults.rst>`_, optional):

       Information about any fault in case Storage DRS failed to make a recommendation.
    task (`vim.Task <vim/Task.rst>`_, optional):

       The ID of the task, which monitors the storage placement or datastore entering maintennace mode operation.
