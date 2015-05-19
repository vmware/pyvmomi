.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vim.HostSystem: ../../../vim/HostSystem.rst

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _AnswerFileStatusResult: ../../../vim/profile/host/AnswerFileStatusResult.rst

.. _HostProfileManagerAnswerFileStatus: ../../../vim/profile/host/ProfileManager/AnswerFileStatus.rst

.. _vim.profile.host.AnswerFileStatusResult.AnswerFileStatusError: ../../../vim/profile/host/AnswerFileStatusResult/AnswerFileStatusError.rst


vim.profile.host.AnswerFileStatusResult
=======================================
  The `AnswerFileStatusResult`_ data object shows the validity of the answer file associated with a host.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    checkedTime (`datetime`_):

       Time that the answer file status was determined.
    host (`vim.HostSystem`_):

       Host associated with the answer file.
    status (`str`_):

       Status of the answer file. See `HostProfileManagerAnswerFileStatus`_ for valid values.
    error ([`vim.profile.host.AnswerFileStatusResult.AnswerFileStatusError`_], optional):

       Ifstatusisinvalid, this property contains a list of status error objects.
