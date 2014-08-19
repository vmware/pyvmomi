
vim.host.MaintenanceSpec
========================
  The `HostMaintenanceSpec <vim/host/MaintenanceSpec.rst>`_ data object may be used to specify actions to be taken by a host upon entering maintenance mode. If the `HostMaintenanceSpec <vim/host/MaintenanceSpec.rst>`_ or any of its fields are omitted in a call to `EnterMaintenanceMode_Task <vim/HostSystem.rst#enterMaintenanceMode>`_ , default actions will be chosen as documented for each field's type.See `EnterMaintenanceMode_Task <vim/HostSystem.rst#enterMaintenanceMode>`_ See `VsanHostDecommissionMode <vim/vsan/host/DecommissionMode.rst>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    vsanMode (`vim.vsan.host.DecommissionMode <vim/vsan/host/DecommissionMode.rst>`_, optional):

       The `VsanHostDecommissionMode <vim/vsan/host/DecommissionMode.rst>`_ for this MaintenanceSpec.
