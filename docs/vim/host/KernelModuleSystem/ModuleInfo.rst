.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.KernelModuleSystem.ModuleInfo.SectionInfo: ../../../vim/host/KernelModuleSystem/ModuleInfo/SectionInfo.rst


vim.host.KernelModuleSystem.ModuleInfo
======================================
  Information about a kernel module.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    id (`int`_):

       Module ID.
    name (`str`_):

       Module name.
    version (`str`_):

       Version string.
    filename (`str`_):

       Module filename, without the path.
    optionString (`str`_):

       Option string configured to be passed to the kernel module when loaded. Note that this is not necessarily the option string currently in use by the kernel module.
    loaded (`bool`_):

       Is the module loaded?
    enabled (`bool`_):

       Is the module enabled?
    useCount (`int`_):

       Number of references to this module.
    readOnlySection (`vim.host.KernelModuleSystem.ModuleInfo.SectionInfo`_):

       Read-only section information.
    writableSection (`vim.host.KernelModuleSystem.ModuleInfo.SectionInfo`_):

       Writable section information.
    textSection (`vim.host.KernelModuleSystem.ModuleInfo.SectionInfo`_):

       Text section information.
    dataSection (`vim.host.KernelModuleSystem.ModuleInfo.SectionInfo`_):

       Data section information.
    bssSection (`vim.host.KernelModuleSystem.ModuleInfo.SectionInfo`_):

       BSS section information.
