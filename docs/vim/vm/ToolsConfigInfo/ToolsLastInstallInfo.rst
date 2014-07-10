.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../../vmodl/LocalizedMethodFault.rst


vim.vm.ToolsConfigInfo.ToolsLastInstallInfo
===========================================
  Describes status of last tools upgrade attempt
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    counter (`int`_):

       Number of attempts that have been made to upgrade the version of tools installed on this virtual machine.
    fault (`vmodl.LocalizedMethodFault`_, optional):

       Error that happened, if any, during last attempt to upgrade tools.
