
vim.OvfManager.CreateImportSpecResult
=====================================
  The CreateImportSpecResult contains all information regarding the import that can be extracted from the OVF descriptor.For example, this includes the list of items that the caller must upload in order to complete the import, but not the list of URLs to which the files must be uploaded. These paths are not known until the VMs have been created, ie. until `ResourcePool.importVApp <vim/ResourcePool.rst#importVApp>`_ has been called.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    importSpec (`vim.ImportSpec <vim/ImportSpec.rst>`_, optional):

       The ImportSpec contains information about which `VirtualMachine <vim/VirtualMachine.rst>`_ s and `VirtualApp <vim/VirtualApp.rst>`_ s are present in the entity and how they relate to each other.
    fileItem ([`vim.OvfManager.FileItem <vim/OvfManager/FileItem.rst>`_], optional):

       The files that must be uploaded by the caller as part of importing the entity.The files must be uploaded in order, because some of them may be delta files that patch already-uploaded files.
    warning ([`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_], optional):

       Non-fatal warnings from the processing. The ImportSpec will be valid, but the user may choose to reject it based on these warnings.
    error ([`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_], optional):

       Errors that happened during processing. Something will be wrong with the ImportSpec, or it is not present.
