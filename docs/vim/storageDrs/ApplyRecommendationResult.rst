.. _result: ../../vim/TaskInfo.rst#result

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _RecommendDatastores: ../../vim/StorageResourceManager.rst#recommendDatastores

.. _DatastoreEnterMaintenanceMode: ../../vim/Datastore.rst#enterMaintenanceMode

.. _ApplyStorageDrsRecommendation_Task: ../../vim/StorageResourceManager.rst#applyRecommendation


vim.storageDrs.ApplyRecommendationResult
========================================
  Both `RecommendDatastores`_ and `DatastoreEnterMaintenanceMode`_ methods may invoke Storage DRS for recommendations on placing or evacuating virtual disks. All initial placement recommendations, and some enterMaintenanceMode recommendations need to be approved by the user. Recommendations that are approved will be applied using the `ApplyStorageDrsRecommendation_Task`_ method. This class encapsulates the result of applying a subset of the recommendations.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    vm (`vim.VirtualMachine`_, optional):

       The result applying the recommendation, if it was successful. This is the equivalent of the `result`_ key for the task launched when the recommendation was applied.
