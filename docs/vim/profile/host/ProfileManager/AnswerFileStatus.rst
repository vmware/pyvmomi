vim.profile.host.ProfileManager.AnswerFileStatus
================================================
  The `HostProfileManagerAnswerFileStatus <vim/profile/host/ProfileManager/AnswerFileStatus.rst>`_ enum defines possible values for answer file status.
  :contained by: `vim.profile.host.ProfileManager <vim/profile/host/ProfileManager.rst>`_

  :type: `vim.profile.host.ProfileManager.AnswerFileStatus <vim/profile/host/ProfileManager/AnswerFileStatus.rst>`_

  :name: unknown

values:
--------

unknown
   Answer file status is not known.

valid
   Answer file is valid.

invalid
   Answer file is not valid. The file is either missing or incomplete.
    * To produce an answer file, pass host-specific data (user input) to the
    * `HostProfileManager <vim/profile/host/ProfileManager.rst>`_
    * .
    * `ApplyHostConfig_Task <vim/profile/host/ProfileManager.rst#applyHostConfiguration>`_
    * method.
    * To produce a complete answer file, call the
    * `HostProfile <vim/profile/host/HostProfile.rst>`_
    * .
    * `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_
    * method and fill in any missing parameters in the returned
    * `ProfileExecuteResult <vim/profile/host/ExecuteResult.rst>`_
    * .
    * `requireInput <vim/profile/host/ExecuteResult.rst#requireInput>`_
    * list. After you execute the profile successfully, you can pass the complete required input list to the apply method.
