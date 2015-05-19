.. _vSphere API 4.0: ../../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _vim.host.ConfigSpec: ../../../../vim/host/ConfigSpec.rst

.. _vmodl.LocalizableMessage: ../../../../vmodl/LocalizableMessage.rst

.. _HostProfileManagerConfigTaskList: ../../../../vim/profile/host/ProfileManager/ConfigTaskList.rst


vim.profile.host.ProfileManager.ConfigTaskList
==============================================
  The `HostProfileManagerConfigTaskList`_ data object represents a set of tasks to be performed on a host during host profile application.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    configSpec (`vim.host.ConfigSpec`_, optional):

       Set of configuration changes to be applied to the host.
    taskDescription ([`vmodl.LocalizableMessage`_], optional):

       Description of tasks that will be performed on the host to carry out HostProfile application.
