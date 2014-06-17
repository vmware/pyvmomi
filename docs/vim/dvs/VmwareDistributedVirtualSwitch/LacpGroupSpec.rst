.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _ConfigSpecOperation: ../../../vim/ConfigSpecOperation.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupConfig: ../../../vim/dvs/VmwareDistributedVirtualSwitch/LacpGroupConfig.rst


vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupSpec
====================================================
  This class defines the configuration of a Link Aggregation Control Protocol group.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    lacpGroupConfig (`vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupConfig`_):

       The Link Aggregation Control Protocol group to be configured.
    operation (`str`_):

       Operation type, see `ConfigSpecOperation`_ for valid values.
