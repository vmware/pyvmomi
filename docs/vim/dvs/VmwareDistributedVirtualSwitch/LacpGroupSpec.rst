
vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupSpec
====================================================
  This class defines the configuration of a Link Aggregation Control Protocol group.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    lacpGroupConfig (`vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupConfig <vim/dvs/VmwareDistributedVirtualSwitch/LacpGroupConfig.rst>`_):

       The Link Aggregation Control Protocol group to be configured.
    operation (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Operation type, see `ConfigSpecOperation <vim/ConfigSpecOperation.rst>`_ for valid values.
