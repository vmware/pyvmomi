.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _reason: ../../../vim/host/PatchManager/Status.rst#reason

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostPatchManagerReason: ../../../vim/host/PatchManager/Status/Reason.rst

.. _HostPatchManagerInstallState: ../../../vim/host/PatchManager/Status/InstallState.rst

.. _HostPatchManagerIntegrityStatus: ../../../vim/host/PatchManager/Status/Integrity.rst

.. _vim.host.PatchManager.Status.PrerequisitePatch: ../../../vim/host/PatchManager/Status/PrerequisitePatch.rst


vim.host.PatchManager.Status
============================
  
:extends: vmodl.DynamicData_

Attributes:
    id (`str`_):

       Unique identifier for this update.
    applicable (`bool`_):

       Whether or not this update is applicable to this host. An update may not be applicable to the ESX host for many reasons--for example, it is obsolete, it conflicts with other installed patches or libraries, and so on. The `reason`_ shows some of the reasons why the update is not applicable. An update could be inapplicable with no reason listed. This is because the prerequisite install state is not correct. For example, update A is one of the prerequisites of update B. B not only requires A to be installed, but also requires the host is rebooted after A is installed. When A is installed and the host has not been restarted after the installation, B will not be applicable. In such a case, the scan on both updates A and B would yield a whole picture of the update applicable status.
    reason ([`str`_], optional):

       Possible reasons why an update is not applicable to the ESX host.See `HostPatchManagerReason`_ 
    integrity (`str`_, optional):

       The integrity status of the update's metadata. The value would be unset if the integrity status is unknown to the server.See `HostPatchManagerIntegrityStatus`_ 
    installed (`bool`_):

       Whether the update is installed on the server.
    installState ([`str`_], optional):

       The installation state of the update. Unset if the update is not installed on the server.See `HostPatchManagerInstallState`_ 
    prerequisitePatch ([`vim.host.PatchManager.Status.PrerequisitePatch`_], optional):

       Prerequisite update.
    restartRequired (`bool`_):

       Whether or not this update requires a host restart to take effect.
    reconnectRequired (`bool`_):

       Whether or not this update requires caller to reconnect to the host. This is usually because the update is on the agent that running on the host, the agent would thus be restarted when the update is applied. Caller can reconnect (and possibly relogin) to the host after the agent has been restarted.
    vmOffRequired (`bool`_):

       Whether or not this update requires the host in maintenance mode.
    supersededPatchIds ([`str`_], optional):

       Patches that are superseded by this update.
