
vim.dvs.DistributedVirtualSwitchInfo
====================================
  This class describes a DistributedVirtualSwitch that a device backing can attached to its ports.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    switchName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the switch.
    switchUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The UUID of the switch.
    distributedVirtualSwitch (`vim.DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_):

       The switch.
