
vim.vsan.host.DecommissionMode
==============================
  A `VsanHostDecommissionMode <vim/vsan/host/DecommissionMode.rst>`_ defines an action to take upon decommissioning a host from use with the VSAN service. If the VSAN service DecommissionMode is omitted in a call to `EnterMaintenanceMode_Task <vim/HostSystem.rst#enterMaintenanceMode>`_ , the default action chosen will be `ensureObjectAccessibility <vim/vsan/host/DecommissionMode/ObjectAction.rst#ensureObjectAccessibility>`_ .See `EnterMaintenanceMode_Task <vim/HostSystem.rst#enterMaintenanceMode>`_ See `vsanMode <vim/host/MaintenanceSpec.rst#vsanMode>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    objectAction (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Specifies an action to take with regard to the VSAN service upon putting a host into maintenance mode.See `VsanHostDecommissionModeObjectAction <vim/vsan/host/DecommissionMode/ObjectAction.rst>`_ 
