.. _OvfManager: ../vim/OvfManager.rst

.. _OvfConsumer: ../vim/OvfConsumer.rst

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst

.. _VirtualAppImportSpec: ../vim/vApp/VAppImportSpec.rst

.. _vim.OvfConsumer.OstNode: ../vim/OvfConsumer/OstNode.rst

.. _VirtualMachineImportSpec: ../vim/vm/VmImportSpec.rst

.. _vim.vApp.EntityConfigInfo: ../vim/vApp/EntityConfigInfo.rst


vim.ImportSpec
==============
  An ImportSpec is used when importing VMs or vApps.It can be built from scratch, or it can be generated from an OVF descriptor using the service interface `OvfManager`_ .This class is the abstract base for `VirtualMachineImportSpec`_ and `VirtualAppImportSpec`_ . These three classes form a composite structure that allows us to contain arbitrarily complex entitites in a single ImportSpec.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    entityConfig (`vim.vApp.EntityConfigInfo`_, optional):

       Configuration of sub-entities (virtual machine or vApp). This is used for sub-entities of a vApp that could be a virtual machine or a vApp.
    instantiationOst (`vim.OvfConsumer.OstNode`_, optional):

       The instantiation OST (see `OvfConsumer`_ ) to be consumed by OVF consumers.
