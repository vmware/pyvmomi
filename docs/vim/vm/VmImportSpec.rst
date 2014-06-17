.. _ImportSpec: ../../vim/ImportSpec.rst

.. _VirtualMachine: ../../vim/VirtualMachine.rst

.. _vim.ImportSpec: ../../vim/ImportSpec.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.ResourcePool: ../../vim/ResourcePool.rst

.. _vim.vm.ConfigSpec: ../../vim/vm/ConfigSpec.rst

.. _VirtualAppImportSpec: ../../vim/vApp/VAppImportSpec.rst

.. _ResourcePool.importVApp: ../../vim/ResourcePool.rst#importVApp

.. _VirtualMachineConfigSpec: ../../vim/vm/ConfigSpec.rst


vim.vm.VmImportSpec
===================
  A VmImportSpec is used by `ResourcePool.importVApp`_ when importing entities.It provides all information needed to import a `VirtualMachine`_ . So far, this coincides with `VirtualMachineConfigSpec`_ .A VmImportSpec can be contained in a `VirtualAppImportSpec`_ as part of the ImportSpec for an entity.See also `ImportSpec`_ .
:extends: vim.ImportSpec_
:since: `vSphere API 4.0`_

Attributes:
    configSpec (`vim.vm.ConfigSpec`_):

       Configuration for the virtual machine.
    resPoolEntity (`vim.ResourcePool`_, optional):

       If specified, this resource pool will be used as the parent resource pool and the virtual machine will be made a linked child to the parent vApp. This field is ignored for the root node in an ImportSpec tree.
