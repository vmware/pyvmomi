
vim.fault.ConflictingConfiguration.Config
=========================================
  This class defines the configuration that is in conflict.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_, optional):

       The entity on which the configuration is in conflict.
    propertyPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The property paths that are in conflict.
