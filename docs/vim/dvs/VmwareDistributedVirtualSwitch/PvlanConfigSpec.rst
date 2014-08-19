
vim.dvs.VmwareDistributedVirtualSwitch.PvlanConfigSpec
======================================================
  This class defines the configuration of a PVLAN map entry
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    pvlanEntry (`vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry <vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst>`_):

       The PVLAN entry to be added or removed.
    operation (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Operation type. See `ConfigSpecOperation <vim/ConfigSpecOperation.rst>`_ for valid values, except for the "edit" value, which is not supported.
