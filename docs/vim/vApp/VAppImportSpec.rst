.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VirtualApp: ../../vim/VirtualApp.rst

.. _ImportSpec: ../../vim/ImportSpec.rst

.. _VirtualMachine: ../../vim/VirtualMachine.rst

.. _vim.ImportSpec: ../../vim/ImportSpec.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.ResourceConfigSpec: ../../vim/ResourceConfigSpec.rst

.. _vim.vApp.VAppConfigSpec: ../../vim/vApp/VAppConfigSpec.rst

.. _ResourcePool.importVApp: ../../vim/ResourcePool.rst#importVApp


vim.vApp.VAppImportSpec
=======================
  A VAppImportSpec is used by `ResourcePool.importVApp`_ when importing vApps (single VM or multi-VM).It provides all information needed to import a `VirtualApp`_ .See also `ImportSpec`_ .
:extends: vim.ImportSpec_
:since: `vSphere API 4.0`_

Attributes:
    name (`str`_):

       The name of the vApp
    vAppConfigSpec (`vim.vApp.VAppConfigSpec`_):

       vApp configuration
    resourcePoolSpec (`vim.ResourceConfigSpec`_):

       Resource pool specification.If resourcePoolSpec.entity is specified, that resource pool is used as the parent resource pool and the vApp will be made a linked child to the parent vApp. This field is ignored for the root node in an ImportSpec tree. Use of resourcePoolSpec.entity for creating linked children is deprecated as of vSphere API 5.1.
    child ([`vim.ImportSpec`_], optional):

       Contains a list of children ( `VirtualMachine`_ s and `VirtualApp`_ s).
