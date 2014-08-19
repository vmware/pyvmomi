
vim.profile.host.AnswerFileStatusResult
=======================================
  The `AnswerFileStatusResult <vim/profile/host/AnswerFileStatusResult.rst>`_ data object shows the validity of the answer file associated with a host.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    checkedTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       Time that the answer file status was determined.
    host (`vim.HostSystem <vim/HostSystem.rst>`_):

       Host associated with the answer file.
    status (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Status of the answer file. See `HostProfileManagerAnswerFileStatus <vim/profile/host/ProfileManager/AnswerFileStatus.rst>`_ for valid values.
    error ([`vim.profile.host.AnswerFileStatusResult.AnswerFileStatusError <vim/profile/host/AnswerFileStatusResult/AnswerFileStatusError.rst>`_], optional):

       Ifstatusisinvalid, this property contains a list of status error objects.
