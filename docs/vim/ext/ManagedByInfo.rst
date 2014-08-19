
vim.ext.ManagedByInfo
=====================
  The ManagedByInfo data object contains information about the extension responsible for the life-cycle of the entity.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    extensionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Key of the extension managing the entity.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Managed entity type, as defined by the extension managing the entity. An extension can manage different types of entities - different kinds of virtual machines, vApps, etc. - and this property is used to find the corresponding `managedEntityInfo <vim/ext/ManagedEntityInfo.rst>`_ entry from the extension.
