.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vim.option.OptionDef: ../../vim/option/OptionDef.rst

.. _vim.fault.InvalidName: ../../vim/fault/InvalidName.rst

.. _vim.option.OptionValue: ../../vim/option/OptionValue.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst


vim.option.OptionManager
========================
  This managed object type is used for managing key/value pair options.
   * You can define options on the fly, in a logical tree using a dot notation for keys. For example, "Ethernet.Connection" describes the Connection option as child of the Ethernet option.
   * You can use the queryMethod to retrieve a single property or a subset of properties based on the dot notation path.
   * 




Attributes
----------
    supportedOption ([`vim.option.OptionDef`_]):
       A list of supported key/value pair options including their type information.
    setting ([`vim.option.OptionValue`_]):
       A list of the current settings for the key/value pair options.


Methods
-------


QueryOptions(name):
   Returns a specific node or nodes in the option hierarchy.This method might require any of the following privileges depending on where the property fits in the inventory tree.
    * System.View on the root folder, if this is used to read settings in the
    * client
    * subtree.
    * System.Read on the root folder, if this is used to read all settings or any settings beside those in the
    * client
    * subtree.
    * System.Read on the host, if this is used to read the advanced options for a host configuration.
    * 


  Privilege:
               System.View



  Args:
    name (`str`_, optional):




  Returns:
    [`vim.option.OptionValue`_]:
         The option with the given name. If the name ends with a dot, all options for that subtree are returned.

  Raises:

    `vim.fault.InvalidName`_: 
       if no option or subtree exists with the given name.


UpdateOptions(changedValue):
   Updates one or more properties. These properties are changed atomically: either all are applied or none are.A nested option setting can be named using a dot notation; for example, system.cacheSize.This method might require any of the following privileges depending on where the property fits in the inventory tree.
    * Global.Settings on the root folder, if this is used to modify the settings in the service node.
    * Host.Config.AdvancedConfig on the host, if this is used to set the advanced options in the host configuration.
    * 


  Privilege:
               dynamic



  Args:
    changedValue (`vim.option.OptionValue`_):




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidName`_: 
       if one or more OptionValue objects refers to a non-existent option.

    `vmodl.fault.InvalidArgument`_: 
       if one or more OptionValue contains an invalid value.


