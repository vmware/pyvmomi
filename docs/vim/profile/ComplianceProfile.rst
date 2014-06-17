.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.profile.Expression: ../../vim/profile/Expression.rst


vim.profile.ComplianceProfile
=============================
  DataObject contains the verifications that need to be done to make sure the entity is in compliance.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    expression (`vim.profile.Expression`_):

       List of expressions that make up the ComplianceChecks.
    rootExpression (`str`_):

       Name of the Expression which is the root of the expression tree.
