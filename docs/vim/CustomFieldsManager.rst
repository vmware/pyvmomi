.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst

.. _vim.PrivilegePolicyDef: ../vim/PrivilegePolicyDef.rst

.. _vim.fault.DuplicateName: ../vim/fault/DuplicateName.rst

.. _vim.fault.InvalidPrivilege: ../vim/fault/InvalidPrivilege.rst

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.CustomFieldsManager.FieldDef: ../vim/CustomFieldsManager/FieldDef.rst


vim.CustomFieldsManager
=======================
  The CustomFieldsManager object is used to add and remove custom fields to managed entities.The custom fields values set on managed entities are available through the `customValue`_ property and through the summary objects for `VirtualMachine`_ and `HostSystem`_ . They are not available directly through this managed object.This functionality is only available through VirtualCenter.




Attributes
----------
    field ([`vim.CustomFieldsManager.FieldDef`_]):
      privilege: System.View
       List of custom fields defined on this server. The fields are sorted by name.


Methods
-------


AddCustomFieldDef(name, moType, fieldDefPolicy, fieldPolicy):
   Creates a new custom field. If the moType is specified, the field will only be available for that type of managed object.


  Privilege:
               Global.ManageCustomFields



  Args:
    name (`str`_):
       The name of the field.


    moType (`str`_, optional, since `VI API 2.5`_ ):
       The managed object type to which this field will apply


    fieldDefPolicy (`vim.PrivilegePolicyDef`_, optional, since `VI API 2.5`_ ):
       Privilege policy to apply to FieldDef being created


    fieldPolicy (`vim.PrivilegePolicyDef`_, optional, since `VI API 2.5`_ ):
       Privilege policy to apply to instances of field




  Returns:
    `vim.CustomFieldsManager.FieldDef`_:
         

  Raises:

    `vim.fault.DuplicateName`_: 
       if a custom field with the name already exists.

    `vim.fault.InvalidPrivilege`_: 
       if a specified privilege is not defined.


RemoveCustomFieldDef(key):
   Removes a custom field. This also removes all values assigned to this custom field.


  Privilege:
               Global.ManageCustomFields



  Args:
    key (`int`_):
       The unique key for the field definition.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       if no custom field with that key exists.


RenameCustomFieldDef(key, name):
   Renames a custom field.


  Privilege:
               Global.ManageCustomFields



  Args:
    key (`int`_):
       The unique key for the field definition.


    name (`str`_):
       The new name for the field.




  Returns:
    None
         

  Raises:

    `vim.fault.DuplicateName`_: 
       if a custom field with the name already exists.

    `vmodl.fault.InvalidArgument`_: 
       if no custom field with that key exists.


SetField(entity, key, value):
   Assigns a value to a custom field on an entity.


  Privilege:



  Args:
    entity (`vim.ManagedEntity`_):


    key (`int`_):


    value (`str`_):




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       if no custom field with that key exists.


