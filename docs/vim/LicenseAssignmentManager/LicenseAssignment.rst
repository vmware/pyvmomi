.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vmodl.KeyAnyValue: ../../vmodl/KeyAnyValue.rst

.. _vim.LicenseManager.LicenseInfo: ../../vim/LicenseManager/LicenseInfo.rst


vim.LicenseAssignmentManager.LicenseAssignment
==============================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    entityId (`str`_):

       Id for the entity
    scope (`str`_, optional):

       Scope of the entityId
    entityDisplayName (`str`_, optional):

       Display name of the entity
    assignedLicense (`vim.LicenseManager.LicenseInfo`_):

       License assigned to the entity
    properties ([`vmodl.KeyAnyValue`_], optional):

       Additional properties associated with this assignment Some of the properties are: "inUseFeatures" -- Features in the license key that are being used by the entity "ProductName" -- Name of the entity. Should match the product name of the assigned license. "ProductVersion" -- Version of the entity. Should match the product version of the assigned license. "Evaluation" -- EvaluationInfo object representing the evaluation left for the entity.
