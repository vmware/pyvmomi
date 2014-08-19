
vim.profile.host.ProfileManager.ConfigTaskList
==============================================
  The `HostProfileManagerConfigTaskList <vim/profile/host/ProfileManager/ConfigTaskList.rst>`_ data object represents a set of tasks to be performed on a host during host profile application.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    configSpec (`vim.host.ConfigSpec <vim/host/ConfigSpec.rst>`_, optional):

       Set of configuration changes to be applied to the host.
    taskDescription ([`vmodl.LocalizableMessage <vmodl/LocalizableMessage.rst>`_], optional):

       Description of tasks that will be performed on the host to carry out HostProfile application.
