.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.PrivilegePolicyDef: ../../vim/PrivilegePolicyDef.rst


vim.CustomFieldsManager.FieldDef
================================
  Describes a custom field.
:extends: vmodl.DynamicData_

Attributes:
    key (`int`_):

       A unique ID used to reference this custom field in assignments. This ID is unique for the lifetime of the field (even across rename operations).
    name (`str`_):

       Name of the field.
    type (`str`_):

       Type of the field.
    managedObjectType (`str`_, optional):

       Type of object for which the field is valid. If not specified, the field is valid for all managed objects.
    fieldDefPrivileges (`vim.PrivilegePolicyDef`_, optional):

       The set of privileges to apply on this field definition
    fieldInstancePrivileges (`vim.PrivilegePolicyDef`_, optional):

       The set of privileges to apply on instances of this field
