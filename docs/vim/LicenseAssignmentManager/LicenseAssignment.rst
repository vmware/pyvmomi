
vim.LicenseAssignmentManager.LicenseAssignment
==============================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    entityId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Id for the entity
    scope (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Scope of the entityId
    entityDisplayName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Display name of the entity
    assignedLicense (`vim.LicenseManager.LicenseInfo <vim/LicenseManager/LicenseInfo.rst>`_):

       License assigned to the entity
    properties ([`vmodl.KeyAnyValue <vmodl/KeyAnyValue.rst>`_], optional):

       Additional properties associated with this assignment Some of the properties are: "inUseFeatures" -- Features in the license key that are being used by the entity "ProductName" -- Name of the entity. Should match the product name of the assigned license. "ProductVersion" -- Version of the entity. Should match the product version of the assigned license. "Evaluation" -- EvaluationInfo object representing the evaluation left for the entity.
