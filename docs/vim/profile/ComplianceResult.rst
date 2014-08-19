
vim.profile.ComplianceResult
============================
  DataObject representing the result from a ComplianceCheck
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    profile (`vim.profile.Profile <vim/profile/Profile.rst>`_, optional):

       Profile for which the ComplianceResult applies
    complianceStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates the compliance status of the entity. See
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_, optional):

       Entity on which the compliance check was carried out. Entity can be a Cluster, Host and so on.
    checkTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Time at which compliance check was last run on the entity
    failure ([`vim.profile.ComplianceResult.ComplianceFailure <vim/profile/ComplianceResult/ComplianceFailure.rst>`_], optional):

       If complianceStatus is non-compliant, failure will contain additional information about the compliance errors.
