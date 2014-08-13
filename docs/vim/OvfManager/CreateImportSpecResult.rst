.. _VirtualApp: ../../vim/VirtualApp.rst

.. _VirtualMachine: ../../vim/VirtualMachine.rst

.. _vim.ImportSpec: ../../vim/ImportSpec.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ResourcePool.importVApp: ../../vim/ResourcePool.rst#importVApp

.. _vim.OvfManager.FileItem: ../../vim/OvfManager/FileItem.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.OvfManager.CreateImportSpecResult
=====================================
  The CreateImportSpecResult contains all information regarding the import that can be extracted from the OVF descriptor.For example, this includes the list of items that the caller must upload in order to complete the import, but not the list of URLs to which the files must be uploaded. These paths are not known until the VMs have been created, ie. until `ResourcePool.importVApp`_ has been called.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    importSpec (`vim.ImportSpec`_, optional):

       The ImportSpec contains information about which `VirtualMachine`_ s and `VirtualApp`_ s are present in the entity and how they relate to each other.
    fileItem ([`vim.OvfManager.FileItem`_], optional):

       The files that must be uploaded by the caller as part of importing the entity.The files must be uploaded in order, because some of them may be delta files that patch already-uploaded files.
    warning ([`vmodl.LocalizedMethodFault`_], optional):

       Non-fatal warnings from the processing. The ImportSpec will be valid, but the user may choose to reject it based on these warnings.
    error ([`vmodl.LocalizedMethodFault`_], optional):

       Errors that happened during processing. Something will be wrong with the ImportSpec, or it is not present.
