vim.vApp.CloneSpec.ProvisioningType
===================================
  The cloned VMs can either be provisioned the same way as the VMs they are a clone of, thin provisioned or thick provisioned, or linked clones (i.e., using delta disks).
  :contained by: `vim.vApp.CloneSpec <vim/vApp/CloneSpec.rst>`_

  :type: `vim.vApp.CloneSpec.ProvisioningType <vim/vApp/CloneSpec/ProvisioningType.rst>`_

  :name: thick

values:
--------

sameAsSource
   Each disk in the cloned virtual machines will have the same type of disk as the source vApp.

thick
   Each disk in the cloned virtual machines are allocated and committed in full size immediately.

thin
   Each disk in the cloned virtual machines is allocated in full size now and committed on demand. This is only supported on VMFS-3 and newer datastores. Other types of datastores may create thick disks.
