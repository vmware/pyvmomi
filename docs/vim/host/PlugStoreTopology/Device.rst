.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.host.ScsiLun: ../../../vim/host/ScsiLun.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.PlugStoreTopology.Path: ../../../vim/host/PlugStoreTopology/Path.rst


vim.host.PlugStoreTopology.Device
=================================
  This data object type is an association class that describes a ScsiLun and its associated Path objects. The ScsiLun is a Device that is formed from a set of Paths.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       Linkable identifier.
    lun (`vim.host.ScsiLun`_):

       The SCSI device corresponding to logical unit.
    path (`vim.host.PlugStoreTopology.Path`_, optional):

       The array of paths available to access this LogicalUnit.
