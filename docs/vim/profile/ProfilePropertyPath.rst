.. _str: https://docs.python.org/2/library/stdtypes.html

.. _parameter: ../../vim/profile/PolicyOption.rst#parameter

.. _PolicyOption: ../../vim/profile/PolicyOption.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ProfilePropertyPath: ../../vim/profile/ProfilePropertyPath.rst


vim.profile.ProfilePropertyPath
===============================
  The `ProfilePropertyPath`_ data object represents the path to a profile, policy option, or specific parameter. IfprofilePath,policyId, andparameterIdare all specified, the combination of the three identifies a particular parameter. If onlyprofilePathandpolicyIdare specified, the combination identifies a specific profile policy option. If just theprofilePathis specified, the data object identifies a profile instance.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    profilePath (`str`_):

       Complete path to the leaf profile, relative to the root of the host profile document.
    policyId (`str`_, optional):

       Policy option identifier. See `PolicyOption`_ . `id`_ .
    parameterId (`str`_, optional):

       Key for a parameter in the policy specified bypolicyId. See `PolicyOption`_ . `parameter`_ and `key`_ .
