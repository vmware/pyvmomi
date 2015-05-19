.. _str: https://docs.python.org/2/library/stdtypes.html

.. _nativeFormat: ../../../../vim/vm/device/VirtualDisk/DeltaDiskFormat.rst#nativeFormat

.. _redoLogFormat: ../../../../vim/vm/device/VirtualDisk/DeltaDiskFormat.rst#redoLogFormat

.. _vSphere API 5.1: ../../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _vim.option.ChoiceOption: ../../../../vim/option/ChoiceOption.rst


vim.vm.device.VirtualDiskOption.DeltaDiskFormatsSupported
=========================================================
  Delta disk format supported for each datastore type.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    datastoreType (`str`_):

       Datastore type name
    deltaDiskFormat (`vim.option.ChoiceOption`_):

       Delta disk formats supported. Valid values are:
        * `redoLogFormat`_
        * 
        * `nativeFormat`_
        * 
        * 
