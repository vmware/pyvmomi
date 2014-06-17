.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _managedEntityInfo: ../../vim/ext/ManagedEntityInfo.rst


vim.ext.ManagedByInfo
=====================
  The ManagedByInfo data object contains information about the extension responsible for the life-cycle of the entity.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    extensionKey (`str`_):

       Key of the extension managing the entity.
    type (`str`_):

       Managed entity type, as defined by the extension managing the entity. An extension can manage different types of entities - different kinds of virtual machines, vApps, etc. - and this property is used to find the corresponding `managedEntityInfo`_ entry from the extension.
