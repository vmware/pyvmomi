
vim.profile.ProfilePropertyPath
===============================
  The `ProfilePropertyPath <vim/profile/ProfilePropertyPath.rst>`_ data object represents the path to a profile, policy option, or specific parameter. IfprofilePath,policyId, andparameterIdare all specified, the combination of the three identifies a particular parameter. If onlyprofilePathandpolicyIdare specified, the combination identifies a specific profile policy option. If just theprofilePathis specified, the data object identifies a profile instance.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    profilePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Complete path to the leaf profile, relative to the root of the host profile document.
    policyId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Policy option identifier. See `PolicyOption <vim/profile/PolicyOption.rst>`_ . `id <vim/profile/PolicyOption.rst#id>`_ .
    parameterId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Key for a parameter in the policy specified bypolicyId. See `PolicyOption <vim/profile/PolicyOption.rst>`_ . `parameter <vim/profile/PolicyOption.rst#parameter>`_ and `key <vmodl/KeyAnyValue.rst#key>`_ .
