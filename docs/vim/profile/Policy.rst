.. _str: https://docs.python.org/2/library/stdtypes.html

.. _ProfilePolicy: ../../vim/profile/Policy.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.profile.PolicyOption: ../../vim/profile/PolicyOption.rst


vim.profile.Policy
==================
  The `ProfilePolicy`_ data object represents a policy.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    id (`str`_):

       Identifier for the policy.
    policyOption (`vim.profile.PolicyOption`_):

       Configuration parameters.
