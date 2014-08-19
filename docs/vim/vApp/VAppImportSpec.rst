
vim.vApp.VAppImportSpec
=======================
  A VAppImportSpec is used by `ResourcePool.importVApp <vim/ResourcePool.rst#importVApp>`_ when importing vApps (single VM or multi-VM).It provides all information needed to import a `VirtualApp <vim/VirtualApp.rst>`_ .See also `ImportSpec <vim/ImportSpec.rst>`_ .
:extends: vim.ImportSpec_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the vApp
    vAppConfigSpec (`vim.vApp.VAppConfigSpec <vim/vApp/VAppConfigSpec.rst>`_):

       vApp configuration
    resourcePoolSpec (`vim.ResourceConfigSpec <vim/ResourceConfigSpec.rst>`_):

       Resource pool specification.If resourcePoolSpec.entity is specified, that resource pool is used as the parent resource pool and the vApp will be made a linked child to the parent vApp. This field is ignored for the root node in an ImportSpec tree. Use of resourcePoolSpec.entity for creating linked children is deprecated as of vSphere API 5.1.
    child ([`vim.ImportSpec <vim/ImportSpec.rst>`_], optional):

       Contains a list of children ( `VirtualMachine <vim/VirtualMachine.rst>`_ s and `VirtualApp <vim/VirtualApp.rst>`_ s).
