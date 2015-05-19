.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vsanMode: ../../../vim/host/MaintenanceSpec.rst#vsanMode

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VsanHostDecommissionMode: ../../../vim/vsan/host/DecommissionMode.rst

.. _EnterMaintenanceMode_Task: ../../../vim/HostSystem.rst#enterMaintenanceMode

.. _ensureObjectAccessibility: ../../../vim/vsan/host/DecommissionMode/ObjectAction.rst#ensureObjectAccessibility

.. _VsanHostDecommissionModeObjectAction: ../../../vim/vsan/host/DecommissionMode/ObjectAction.rst


vim.vsan.host.DecommissionMode
==============================
  A `VsanHostDecommissionMode`_ defines an action to take upon decommissioning a host from use with the VSAN service. If the VSAN service DecommissionMode is omitted in a call to `EnterMaintenanceMode_Task`_ , the default action chosen will be `ensureObjectAccessibility`_ .See `EnterMaintenanceMode_Task`_ See `vsanMode`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    objectAction (`str`_):

       Specifies an action to take with regard to the VSAN service upon putting a host into maintenance mode.See `VsanHostDecommissionModeObjectAction`_ 
