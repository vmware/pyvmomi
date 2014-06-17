.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.profile.ProfilePropertyPath: ../../vim/profile/ProfilePropertyPath.rst


vim.profile.ComplianceLocator
=============================
  This dataObject contains information about location of applyProfile which was responsible for generation of a particular ComplianceExpression.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    expressionName (`str`_):

       Exression for which the Locator corresponds to
    applyPath (`vim.profile.ProfilePropertyPath`_):

       Complete path to the profile/policy which was responsible for the generation of the ComplianceExpression. [ProfilePath + policyId] will uniquely identify a Policy.
