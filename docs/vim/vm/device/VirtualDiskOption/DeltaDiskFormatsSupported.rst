
vim.vm.device.VirtualDiskOption.DeltaDiskFormatsSupported
=========================================================
  Delta disk format supported for each datastore type.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    datastoreType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Datastore type name
    deltaDiskFormat (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       Delta disk formats supported. Valid values are:
        * `redoLogFormat <vim/vm/device/VirtualDisk/DeltaDiskFormat.rst#redoLogFormat>`_
        * 
        * `nativeFormat <vim/vm/device/VirtualDisk/DeltaDiskFormat.rst#nativeFormat>`_
        * 
        * 
