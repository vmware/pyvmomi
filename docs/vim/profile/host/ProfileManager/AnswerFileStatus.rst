.. _HostProfile: ../../../../vim/profile/host/HostProfile.rst

.. _requireInput: ../../../../vim/profile/host/ExecuteResult.rst#requireInput

.. _HostProfileManager: ../../../../vim/profile/host/ProfileManager.rst

.. _ExecuteHostProfile: ../../../../vim/profile/host/HostProfile.rst#execute

.. _ApplyHostConfig_Task: ../../../../vim/profile/host/ProfileManager.rst#applyHostConfiguration

.. _ProfileExecuteResult: ../../../../vim/profile/host/ExecuteResult.rst

.. _vim.profile.host.ProfileManager: ../../../../vim/profile/host/ProfileManager.rst

.. _HostProfileManagerAnswerFileStatus: ../../../../vim/profile/host/ProfileManager/AnswerFileStatus.rst

.. _vim.profile.host.ProfileManager.AnswerFileStatus: ../../../../vim/profile/host/ProfileManager/AnswerFileStatus.rst

vim.profile.host.ProfileManager.AnswerFileStatus
================================================
  The `HostProfileManagerAnswerFileStatus`_ enum defines possible values for answer file status.
  :contained by: `vim.profile.host.ProfileManager`_

  :type: `vim.profile.host.ProfileManager.AnswerFileStatus`_

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
    * `HostProfileManager`_
    * .
    * `ApplyHostConfig_Task`_
    * method.
    * To produce a complete answer file, call the
    * `HostProfile`_
    * .
    * `ExecuteHostProfile`_
    * method and fill in any missing parameters in the returned
    * `ProfileExecuteResult`_
    * .
    * `requireInput`_
    * list. After you execute the profile successfully, you can pass the complete required input list to the apply method.
