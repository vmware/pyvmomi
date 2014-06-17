.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _ConfigSpecOperation: ../../../vim/ConfigSpecOperation.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst


vim.dvs.VmwareDistributedVirtualSwitch.PvlanConfigSpec
======================================================
  This class defines the configuration of a PVLAN map entry
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    pvlanEntry (`vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry`_):

       The PVLAN entry to be added or removed.
    operation (`str`_):

       Operation type. See `ConfigSpecOperation`_ for valid values, except for the "edit" value, which is not supported.
