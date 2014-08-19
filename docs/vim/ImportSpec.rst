
vim.ImportSpec
==============
  An ImportSpec is used when importing VMs or vApps.It can be built from scratch, or it can be generated from an OVF descriptor using the service interface `OvfManager <vim/OvfManager.rst>`_ .This class is the abstract base for `VirtualMachineImportSpec <vim/vm/VmImportSpec.rst>`_ and `VirtualAppImportSpec <vim/vApp/VAppImportSpec.rst>`_ . These three classes form a composite structure that allows us to contain arbitrarily complex entitites in a single ImportSpec.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    entityConfig (`vim.vApp.EntityConfigInfo <vim/vApp/EntityConfigInfo.rst>`_, optional):

       Configuration of sub-entities (virtual machine or vApp). This is used for sub-entities of a vApp that could be a virtual machine or a vApp.
    instantiationOst (`vim.OvfConsumer.OstNode <vim/OvfConsumer/OstNode.rst>`_, optional):

       The instantiation OST (see `OvfConsumer <vim/OvfConsumer.rst>`_ ) to be consumed by OVF consumers.
