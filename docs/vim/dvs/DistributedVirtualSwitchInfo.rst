.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.DistributedVirtualSwitch: ../../vim/DistributedVirtualSwitch.rst


vim.dvs.DistributedVirtualSwitchInfo
====================================
  This class describes a DistributedVirtualSwitch that a device backing can attached to its ports.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    switchName (`str`_):

       The name of the switch.
    switchUuid (`str`_):

       The UUID of the switch.
    distributedVirtualSwitch (`vim.DistributedVirtualSwitch`_):

       The switch.
