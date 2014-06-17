.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.ManagedEntity: ../../../vim/ManagedEntity.rst


vim.fault.ConflictingConfiguration.Config
=========================================
  This class defines the configuration that is in conflict.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    entity (`vim.ManagedEntity`_, optional):

       The entity on which the configuration is in conflict.
    propertyPath (`str`_):

       The property paths that are in conflict.
