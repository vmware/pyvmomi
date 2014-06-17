.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.HostSystem: ../../../vim/HostSystem.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.HostSlots
=========================================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    host (`vim.HostSystem`_):

       The reference to the host.
    slots (`int`_):

       The number of slots in this host.
