
vim.profile.ComplianceProfile
=============================
  DataObject contains the verifications that need to be done to make sure the entity is in compliance.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    expression ([`vim.profile.Expression <vim/profile/Expression.rst>`_]):

       List of expressions that make up the ComplianceChecks.
    rootExpression (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the Expression which is the root of the expression tree.
