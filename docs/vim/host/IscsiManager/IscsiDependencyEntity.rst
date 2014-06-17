.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.IscsiManager.IscsiDependencyEntity
===========================================
  Defines a dependency entity. Contains the affected Virtual NIC device name and iSCSI HBA name (if Virtual NIC is associated with the HBA). See IscsiMigrationDependency
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    pnicDevice (`str`_):

       The affected Physical NIC device
    vnicDevice (`str`_):

       The affected Virtual NIC device
    vmhbaName (`str`_):

       The iSCSI HBA that the Virtual NIC is associated with, if any.
