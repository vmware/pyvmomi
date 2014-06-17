.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.vm.DeviceRuntimeInfo.DeviceRuntimeState: ../../vim/vm/DeviceRuntimeInfo/DeviceRuntimeState.rst


vim.vm.DeviceRuntimeInfo
========================
  The DeviceRuntimeInfo data object type provides information about the execution state of a single virtual device.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    runtimeState (`vim.vm.DeviceRuntimeInfo.DeviceRuntimeState`_):

       The device runtime state.
    key (`int`_):

       The device key.
