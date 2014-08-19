
vim.OvfManager.CreateImportSpecParams
=====================================
  Parameters for deploying an OVF.
:extends: vim.OvfManager.CommonParams_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    entityName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name to set on the entity (more precisely, on the top-level vApp or VM of the entity) as it appears in VI. If empty, the product name is obtained from the ProductSection of the descriptor. If that name is not specified, the ovf:id of the top-level entity is used.
    hostSystem (`vim.HostSystem <vim/HostSystem.rst>`_, optional):

       The host to validate the OVF descriptor against, if it cannot be deduced from the resource pool.The privilege System.Read is required on the host.
    networkMapping ([`vim.OvfManager.NetworkMapping <vim/OvfManager/NetworkMapping.rst>`_], optional):

       The mapping of network identifiers from the descriptor to networks in the VI infrastructure.The privilege Network.Assign is required on all networks in the list.
    ipAllocationPolicy (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The IP allocation policy chosen by the caller.See `VAppIPAssignmentInfo <vim/vApp/IPAssignmentInfo.rst>`_ .
    ipProtocol (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The IP protocol chosen by the caller.See `VAppIPAssignmentInfo <vim/vApp/IPAssignmentInfo.rst>`_ .
    propertyMapping ([`vim.KeyValue <vim/KeyValue.rst>`_], optional):

       The assignment of values to the properties found in the descriptor. If no value is specified for an option, the default value from the descriptor is used.
    resourceMapping ([`vim.OvfManager.ResourceMap <vim/OvfManager/ResourceMap.rst>`_], optional):

       The resource configuration for the created vApp. This can be used to distribute a vApp across multiple resource pools (and create linked children).
    diskProvisioning (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       An optional disk provisioning. If set, all the disks in the deployed OVF will have get the same specified disk type (e.g., thin provisioned). The valide values for disk provisioning are:
        * `monolithicSparse <vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#monolithicSparse>`_
        * 
        * `monolithicFlat <vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#monolithicFlat>`_
        * 
        * `twoGbMaxExtentSparse <vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#twoGbMaxExtentSparse>`_
        * 
        * `twoGbMaxExtentFlat <vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#twoGbMaxExtentFlat>`_
        * 
        * `thin <vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#thin>`_
        * 
        * `thick <vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#thick>`_
        * 
        * `sparse <vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#sparse>`_
        * 
        * `flat <vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#flat>`_
        * 
        * `seSparse <vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#seSparse>`_
        * 
        * See
        * `VirtualDiskMode <vim/vm/device/VirtualDiskOption/DiskMode.rst>`_
        * 
    instantiationOst (`vim.OvfConsumer.OstNode <vim/OvfConsumer/OstNode.rst>`_, optional):

       The instantiation OST to configure OVF consumers. This is created by the client from the annotated OST. See `OvfConsumer <vim/OvfConsumer.rst>`_ for details.
