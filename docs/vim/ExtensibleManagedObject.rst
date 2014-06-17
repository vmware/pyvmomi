.. _str: https://docs.python.org/2/library/stdtypes.html

.. _name: ../vim/CustomFieldsManager/FieldDef.rst#name

.. _vim.Task: ../vim/Task.rst

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _CustomFieldStringValue: ../vim/CustomFieldsManager/StringValue.rst

.. _fieldInstancePrivileges: ../vim/CustomFieldsManager/FieldDef.rst#fieldInstancePrivileges

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.CustomFieldsManager.Value: ../vim/CustomFieldsManager/Value.rst

.. _vim.CustomFieldsManager.FieldDef: ../vim/CustomFieldsManager/FieldDef.rst


vim.ExtensibleManagedObject
===========================
   `ExtensibleManagedObject`_ provides methods and properties that provide access to custom fields that may be associated with a managed object. Use the `CustomFieldsManager`_ to define custom fields. The `CustomFieldsManager`_ handles the entire list of custom fields on a server. You can can specify the object type to which a particular custom field applies by setting its `managedObjectType`_ . (If you do not set a managed object type for a custom field definition, the field applies to all managed objects.)




Attributes
----------
    value (`vim.CustomFieldsManager.Value`_):
      privilege: System.View
       List of custom field values. Each value uses a key to associate an instance of a `CustomFieldStringValue`_ with a custom field definition.
    availableField (`vim.CustomFieldsManager.FieldDef`_):
      privilege: System.View
       List of custom field definitions that are valid for the object's type. The fields are sorted by `name`_ .


Methods
-------


setCustomValue(key, value):
   Assigns a value to a custom field. The setCustomValue method requires whichever updatePrivilege is defined as one of the `fieldInstancePrivileges`_ for the CustomFieldDef whose value is being changed.
  since: `VI API 2.5`_


  Privilege:
               dynamic



  Args:
    key (`str`_):
       The name of the field whose value is to be updated.


    value (`str`_):
       Value to be assigned to the custom field.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       if no custom field with that key exists.


