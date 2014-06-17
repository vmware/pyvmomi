.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _RecommendDatastores: ../../vim/StorageResourceManager.rst#recommendDatastores

.. _vim.cluster.DrsFaults: ../../vim/cluster/DrsFaults.rst

.. _vim.cluster.Recommendation: ../../vim/cluster/Recommendation.rst

.. _DatastoreEnterMaintenanceMode: ../../vim/Datastore.rst#enterMaintenanceMode


vim.storageDrs.StoragePlacementResult
=====================================
  Both `RecommendDatastores`_ and `DatastoreEnterMaintenanceMode`_ methods may invoke Storage DRS for recommendations on placing or evacuating virtual disks. StoragePlacementResult is the class of the result returned by the methods.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    recommendations (`vim.cluster.Recommendation`_, optional):

       The list of recommendations that the client needs to approve manually.
    drsFault (`vim.cluster.DrsFaults`_, optional):

       Information about any fault in case Storage DRS failed to make a recommendation.
    task (`vim.Task`_, optional):

       The ID of the task, which monitors the storage placement or datastore entering maintennace mode operation.
