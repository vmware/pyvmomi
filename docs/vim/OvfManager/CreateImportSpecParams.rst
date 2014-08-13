.. _str: https://docs.python.org/2/library/stdtypes.html

.. _flat: ../../vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#flat

.. _thin: ../../vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#thin

.. _thick: ../../vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#thick

.. _sparse: ../../vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#sparse

.. _seSparse: ../../vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#seSparse

.. _OvfConsumer: ../../vim/OvfConsumer.rst

.. _vim.KeyValue: ../../vim/KeyValue.rst

.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _monolithicFlat: ../../vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#monolithicFlat

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _VirtualDiskMode: ../../vim/vm/device/VirtualDiskOption/DiskMode.rst

.. _monolithicSparse: ../../vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#monolithicSparse

.. _twoGbMaxExtentFlat: ../../vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#twoGbMaxExtentFlat

.. _VAppIPAssignmentInfo: ../../vim/vApp/IPAssignmentInfo.rst

.. _twoGbMaxExtentSparse: ../../vim/OvfManager/CreateImportSpecParams/DiskProvisioningType.rst#twoGbMaxExtentSparse

.. _vim.OvfConsumer.OstNode: ../../vim/OvfConsumer/OstNode.rst

.. _vim.OvfManager.ResourceMap: ../../vim/OvfManager/ResourceMap.rst

.. _vim.OvfManager.CommonParams: ../../vim/OvfManager/CommonParams.rst

.. _vim.OvfManager.NetworkMapping: ../../vim/OvfManager/NetworkMapping.rst


vim.OvfManager.CreateImportSpecParams
=====================================
  Parameters for deploying an OVF.
:extends: vim.OvfManager.CommonParams_
:since: `vSphere API 4.0`_

Attributes:
    entityName (`str`_):

       The name to set on the entity (more precisely, on the top-level vApp or VM of the entity) as it appears in VI. If empty, the product name is obtained from the ProductSection of the descriptor. If that name is not specified, the ovf:id of the top-level entity is used.
    hostSystem (`vim.HostSystem`_, optional):

       The host to validate the OVF descriptor against, if it cannot be deduced from the resource pool.The privilege System.Read is required on the host.
    networkMapping ([`vim.OvfManager.NetworkMapping`_], optional):

       The mapping of network identifiers from the descriptor to networks in the VI infrastructure.The privilege Network.Assign is required on all networks in the list.
    ipAllocationPolicy (`str`_, optional):

       The IP allocation policy chosen by the caller.See `VAppIPAssignmentInfo`_ .
    ipProtocol (`str`_, optional):

       The IP protocol chosen by the caller.See `VAppIPAssignmentInfo`_ .
    propertyMapping ([`vim.KeyValue`_], optional):

       The assignment of values to the properties found in the descriptor. If no value is specified for an option, the default value from the descriptor is used.
    resourceMapping ([`vim.OvfManager.ResourceMap`_], optional):

       The resource configuration for the created vApp. This can be used to distribute a vApp across multiple resource pools (and create linked children).
    diskProvisioning (`str`_, optional):

       An optional disk provisioning. If set, all the disks in the deployed OVF will have get the same specified disk type (e.g., thin provisioned). The valide values for disk provisioning are:
        * `monolithicSparse`_
        * 
        * `monolithicFlat`_
        * 
        * `twoGbMaxExtentSparse`_
        * 
        * `twoGbMaxExtentFlat`_
        * 
        * `thin`_
        * 
        * `thick`_
        * 
        * `sparse`_
        * 
        * `flat`_
        * 
        * `seSparse`_
        * 
        * See
        * `VirtualDiskMode`_
        * 
    instantiationOst (`vim.OvfConsumer.OstNode`_, optional):

       The instantiation OST to configure OVF consumers. This is created by the client from the annotated OST. See `OvfConsumer`_ for details.
