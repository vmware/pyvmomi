
vim.profile.ComplianceLocator
=============================
  This dataObject contains information about location of applyProfile which was responsible for generation of a particular ComplianceExpression.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    expressionName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Exression for which the Locator corresponds to
    applyPath (`vim.profile.ProfilePropertyPath <vim/profile/ProfilePropertyPath.rst>`_):

       Complete path to the profile/policy which was responsible for the generation of the ComplianceExpression. [ProfilePath + policyId] will uniquely identify a Policy.
