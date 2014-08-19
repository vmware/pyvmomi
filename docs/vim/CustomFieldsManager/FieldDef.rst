
vim.CustomFieldsManager.FieldDef
================================
  Describes a custom field.
:extends: vmodl.DynamicData_

Attributes:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       A unique ID used to reference this custom field in assignments. This ID is unique for the lifetime of the field (even across rename operations).
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the field.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Type of the field.
    managedObjectType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Type of object for which the field is valid. If not specified, the field is valid for all managed objects.
    fieldDefPrivileges (`vim.PrivilegePolicyDef <vim/PrivilegePolicyDef.rst>`_, optional):

       The set of privileges to apply on this field definition
    fieldInstancePrivileges (`vim.PrivilegePolicyDef <vim/PrivilegePolicyDef.rst>`_, optional):

       The set of privileges to apply on instances of this field
