
vim.vm.VmImportSpec
===================
  A VmImportSpec is used by `ResourcePool.importVApp <vim/ResourcePool.rst#importVApp>`_ when importing entities.It provides all information needed to import a `VirtualMachine <vim/VirtualMachine.rst>`_ . So far, this coincides with `VirtualMachineConfigSpec <vim/vm/ConfigSpec.rst>`_ .A VmImportSpec can be contained in a `VirtualAppImportSpec <vim/vApp/VAppImportSpec.rst>`_ as part of the ImportSpec for an entity.See also `ImportSpec <vim/ImportSpec.rst>`_ .
:extends: vim.ImportSpec_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    configSpec (`vim.vm.ConfigSpec <vim/vm/ConfigSpec.rst>`_):

       Configuration for the virtual machine.
    resPoolEntity (`vim.ResourcePool <vim/ResourcePool.rst>`_, optional):

       If specified, this resource pool will be used as the parent resource pool and the virtual machine will be made a linked child to the parent vApp. This field is ignored for the root node in an ImportSpec tree.
