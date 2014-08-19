
vim.storageDrs.ApplyRecommendationResult
========================================
  Both `RecommendDatastores <vim/StorageResourceManager.rst#recommendDatastores>`_ and `DatastoreEnterMaintenanceMode <vim/Datastore.rst#enterMaintenanceMode>`_ methods may invoke Storage DRS for recommendations on placing or evacuating virtual disks. All initial placement recommendations, and some enterMaintenanceMode recommendations need to be approved by the user. Recommendations that are approved will be applied using the `ApplyStorageDrsRecommendation_Task <vim/StorageResourceManager.rst#applyRecommendation>`_ method. This class encapsulates the result of applying a subset of the recommendations.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_, optional):

       The result applying the recommendation, if it was successful. This is the equivalent of the `result <vim/TaskInfo.rst#result>`_ key for the task launched when the recommendation was applied.
