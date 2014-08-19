
vim.CustomFieldsManager
=======================
  The CustomFieldsManager object is used to add and remove custom fields to managed entities.The custom fields values set on managed entities are available through the `customValue <vim/ManagedEntity.rst#customValue>`_ property and through the summary objects for `VirtualMachine <vim/VirtualMachine.rst>`_ and `HostSystem <vim/HostSystem.rst>`_ . They are not available directly through this managed object.This functionality is only available through VirtualCenter.




Attributes
----------
    field ([`vim.CustomFieldsManager.FieldDef <vim/CustomFieldsManager/FieldDef.rst>`_]):
      privilege: System.View
       List of custom fields defined on this server. The fields are sorted by name.


Methods
-------


AddCustomFieldDef(name, moType, fieldDefPolicy, fieldPolicy):
   Creates a new custom field. If the moType is specified, the field will only be available for that type of managed object.


  Privilege:
               Global.ManageCustomFields



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the field.


    moType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional, since `VI API 2.5 <vim/version.rst#vimversionversion2>`_ ):
       The managed object type to which this field will apply


    fieldDefPolicy (`vim.PrivilegePolicyDef <vim/PrivilegePolicyDef.rst>`_, optional, since `VI API 2.5 <vim/version.rst#vimversionversion2>`_ ):
       Privilege policy to apply to FieldDef being created


    fieldPolicy (`vim.PrivilegePolicyDef <vim/PrivilegePolicyDef.rst>`_, optional, since `VI API 2.5 <vim/version.rst#vimversionversion2>`_ ):
       Privilege policy to apply to instances of field




  Returns:
    `vim.CustomFieldsManager.FieldDef <vim/CustomFieldsManager/FieldDef.rst>`_:
         

  Raises:

    `vim.fault.DuplicateName <vim/fault/DuplicateName.rst>`_: 
       if a custom field with the name already exists.

    `vim.fault.InvalidPrivilege <vim/fault/InvalidPrivilege.rst>`_: 
       if a specified privilege is not defined.


RemoveCustomFieldDef(key):
   Removes a custom field. This also removes all values assigned to this custom field.


  Privilege:
               Global.ManageCustomFields



  Args:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The unique key for the field definition.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if no custom field with that key exists.


RenameCustomFieldDef(key, name):
   Renames a custom field.


  Privilege:
               Global.ManageCustomFields



  Args:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The unique key for the field definition.


    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The new name for the field.




  Returns:
    None
         

  Raises:

    `vim.fault.DuplicateName <vim/fault/DuplicateName.rst>`_: 
       if a custom field with the name already exists.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if no custom field with that key exists.


SetField(entity, key, value):
   Assigns a value to a custom field on an entity.


  Privilege:



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):


    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):


    value (`str <https://docs.python.org/2/library/stdtypes.html>`_):




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if no custom field with that key exists.


