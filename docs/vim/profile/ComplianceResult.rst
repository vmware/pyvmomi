.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.profile.Profile: ../../vim/profile/Profile.rst

.. _vim.profile.ComplianceResult.ComplianceFailure: ../../vim/profile/ComplianceResult/ComplianceFailure.rst


vim.profile.ComplianceResult
============================
  DataObject representing the result from a ComplianceCheck
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    profile (`vim.profile.Profile`_, optional):

       Profile for which the ComplianceResult applies
    complianceStatus (`str`_):

       Indicates the compliance status of the entity. See
    entity (`vim.ManagedEntity`_, optional):

       Entity on which the compliance check was carried out. Entity can be a Cluster, Host and so on.
    checkTime (`datetime`_, optional):

       Time at which compliance check was last run on the entity
    failure (`vim.profile.ComplianceResult.ComplianceFailure`_, optional):

       If complianceStatus is non-compliant, failure will contain additional information about the compliance errors.
