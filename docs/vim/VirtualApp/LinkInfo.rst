.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst


vim.VirtualApp.LinkInfo
=======================
  Linked child information.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_
**deprecated**


Attributes:
    key (`vim.ManagedEntity`_):

       The key contains a reference to the entity that is linked to this vApp
    destroyWithParent (`bool`_, optional):

       Whether the entity should be removed, when this vApp is removed
