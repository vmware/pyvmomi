.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _HostPatchManagerInstallState: ../../../../vim/host/PatchManager/Status/InstallState.rst


vim.host.PatchManager.Status.PrerequisitePatch
==============================================
  Updates that are required to be installed before this update can be installed on the server. In addition to being installed on the server, an update can have additional requirement on the server or services running on the server pertaining to the prerequisite update.
:extends: vmodl.DynamicData_

Attributes:
    id (`str`_):

       Unique identifier of the prerequisite update.
    installState (`str`_, optional):

       The requirement on the server or services running on the server pertaining to the prerequisite update. For example, this update could require the server to be rebooted after the prerequisite update is installed. Unset if there is no additional requirement on the prerequisite update.See `HostPatchManagerInstallState`_ 
