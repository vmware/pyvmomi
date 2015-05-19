.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _ovfExportOption: ../../vim/OvfManager.rst#ovfExportOption

.. _vim.vm.Snapshot: ../../vim/vm/Snapshot.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.OvfManager.OvfFile: ../../vim/OvfManager/OvfFile.rst


vim.OvfManager.CreateDescriptorParams
=====================================
  Collection of parameters for createDescriptor
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    ovfFiles ([`vim.OvfManager.OvfFile`_], optional):

       Contains information about the files of the entity, if they have already been downloaded. Needed to construct the References section of the descriptor.OvfFile is a positive list of files to include in the export. An Empty list will do no filtering.
    name (`str`_, optional):

       The ovf:id to use for the top-level OVF Entity. If unset, the entity's product name is used if available. Otherwise, the VI entity name is used.
    description (`str`_, optional):

       The contents of the Annontation section of the top-level OVF Entity. If unset, any existing annotation on the entity is left unchanged.
    includeImageFiles (`bool`_, optional):

       Controls whether attached image files should be included in the descriptor. This applies to image files attached to VirtualCdrom and VirtualFloppy.
    exportOption ([`str`_], optional):

       An optional argument for modifying the export process. The option is used to control what extra information that will be included in the OVF descriptor.To get a list of supported keywords see `ovfExportOption`_ . Unknown options will be ignored by the server.
    snapshot (`vim.vm.Snapshot`_, optional):

       Snapshot reference from which the OVF descriptor should be based.If this parameter is set, the OVF descriptor is based off the snapshot point. This means that the OVF descriptor will have the same configuration as the virtual machine at the time the snapshot was taken.The snapshot must be belong to the specified ManagedEntity in the createDescriptor call.
