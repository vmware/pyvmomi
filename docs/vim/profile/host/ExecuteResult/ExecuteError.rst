.. _vSphere API 4.0: ../../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _ProfileExecuteError: ../../../../vim/profile/host/ExecuteResult/ExecuteError.rst

.. _vmodl.LocalizableMessage: ../../../../vmodl/LocalizableMessage.rst

.. _vim.profile.ProfilePropertyPath: ../../../../vim/profile/ProfilePropertyPath.rst


vim.profile.host.ExecuteResult.ExecuteError
===========================================
  The `ProfileExecuteError`_ data object describes an error encountered during host profile execution.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    path (`vim.profile.ProfilePropertyPath`_, optional):

       Path to the profile or policy with which the error is associated.
    message (`vmodl.LocalizableMessage`_):

       Message describing the error.
