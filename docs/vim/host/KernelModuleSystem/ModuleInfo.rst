
vim.host.KernelModuleSystem.ModuleInfo
======================================
  Information about a kernel module.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    id (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Module ID.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Module name.
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Version string.
    filename (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Module filename, without the path.
    optionString (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Option string configured to be passed to the kernel module when loaded. Note that this is not necessarily the option string currently in use by the kernel module.
    loaded (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Is the module loaded?
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Is the module enabled?
    useCount (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of references to this module.
    readOnlySection (`vim.host.KernelModuleSystem.ModuleInfo.SectionInfo <vim/host/KernelModuleSystem/ModuleInfo/SectionInfo.rst>`_):

       Read-only section information.
    writableSection (`vim.host.KernelModuleSystem.ModuleInfo.SectionInfo <vim/host/KernelModuleSystem/ModuleInfo/SectionInfo.rst>`_):

       Writable section information.
    textSection (`vim.host.KernelModuleSystem.ModuleInfo.SectionInfo <vim/host/KernelModuleSystem/ModuleInfo/SectionInfo.rst>`_):

       Text section information.
    dataSection (`vim.host.KernelModuleSystem.ModuleInfo.SectionInfo <vim/host/KernelModuleSystem/ModuleInfo/SectionInfo.rst>`_):

       Data section information.
    bssSection (`vim.host.KernelModuleSystem.ModuleInfo.SectionInfo <vim/host/KernelModuleSystem/ModuleInfo/SectionInfo.rst>`_):

       BSS section information.
