.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostMaintenanceSpec: ../../vim/host/MaintenanceSpec.rst

.. _VsanHostDecommissionMode: ../../vim/vsan/host/DecommissionMode.rst

.. _EnterMaintenanceMode_Task: ../../vim/HostSystem.rst#enterMaintenanceMode

.. _vim.vsan.host.DecommissionMode: ../../vim/vsan/host/DecommissionMode.rst


vim.host.MaintenanceSpec
========================
  The `HostMaintenanceSpec`_ data object may be used to specify actions to be taken by a host upon entering maintenance mode. If the `HostMaintenanceSpec`_ or any of its fields are omitted in a call to `EnterMaintenanceMode_Task`_ , default actions will be chosen as documented for each field's type.See `EnterMaintenanceMode_Task`_ See `VsanHostDecommissionMode`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    vsanMode (`vim.vsan.host.DecommissionMode`_, optional):

       The `VsanHostDecommissionMode`_ for this MaintenanceSpec.
