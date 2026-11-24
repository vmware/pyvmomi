# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl



class ArrayUpdateSpec(pyVmomi.vmodl.DynamicData):
   """
   An ArrayUpdateSpec data object type is a common superclass
   for supporting incremental updates to arrays.
   
   The common code pattern is:
   
            class MyTypeSpec extrends ArrayUpdateSpec {
                  MyTypeInfo info;
            }
   The ArrayUpdateSpec contains the following:
   - operation: the type of operation being performed.
   - removeKey: In the case of a remove operation, the
     key value that identifies the array to be removed.
   
   Attributes:
       operation: The type of operation being performed on the specified virtual device.
       removeKey: Key for the element to be removed.
           
           Only used if the operation
           is \"remove\".
   """
   class Operation(pyVmomi.VmomiSupport.Enum):
      """
      This list specifies the type of operation being performed on the array.
      
      Attributes:
          add: indicates an addition to the array.
          remove: indicates the removal of an element in the
              array.
              
              In this case the key field must contain the key of the element
              to be removed.
          edit: indicates changes to an element in the array.
      """
      add: _typing.ClassVar['ArrayUpdateSpec.Operation'] = 'add'
      remove: _typing.ClassVar['ArrayUpdateSpec.Operation'] = 'remove'
      edit: _typing.ClassVar['ArrayUpdateSpec.Operation'] = 'edit'

   operation: ArrayUpdateSpec.Operation
   removeKey: _typing.Optional[object] = None


class OptionType(pyVmomi.vmodl.DynamicData):
   """
   The base data object type for all options.
   
   Attributes:
       valueIsReadonly: The flag to indicate whether or not a user
           can modify a value belonging to this option type.
           
           If
           the flag is not set, the value can be modified.
   """
   valueIsReadonly: _typing.Optional[bool] = None

class BoolOption(OptionType):
   """
   The BoolOption data object type describes if an option
   is supported (\"true\") and if the option is set to \"true\" or
   \"false\" by default.
   
   Attributes:
       supported: The flag to indicate whether or not the
           option is supported.
       defaultValue: The default value for the option.
   """
   supported: bool
   defaultValue: bool


class ChoiceOption(OptionType):
   """
   The ChoiceOption data object type defines a set of
   supported string values, a localizable description for each value,
   and the default value.
   
   Attributes:
       choiceInfo: The set of possible selections and descriptions.
       defaultIndex: The index in ChoiceOption.value that serves as the default value.
   """
   choiceInfo: list[pyVmomi.vim.ElementDescription] = []
   defaultIndex: _typing.Optional[int] = None

class FloatOption(OptionType):
   """
   The FloatOption data object type defines the minimum, maximum,
   and default values for a float option.
   
   Attributes:
       min: The minimum value.
       max: The maximum value.
       defaultValue: The default value.
   """
   min: float
   max: float
   defaultValue: float

class IntOption(OptionType):
   """
   The IntOption data object type is used to define the minimum, maximum,
   and default values for an integer option.
   
   Attributes:
       min: The minimum value.
       max: The maximum value.
       defaultValue: The default value.
   """
   min: int
   max: int
   defaultValue: int


class LongOption(OptionType):
   """
   The LongOption data object type is used to define the minimum, maximum,
   and default values for a 64-bit long option.
   
   Attributes:
       min: The minimum value.
       max: The maximum value.
       defaultValue: The default value.
   """
   min: pyVmomi.VmomiSupport.long
   max: pyVmomi.VmomiSupport.long
   defaultValue: pyVmomi.VmomiSupport.long


class OptionDef(pyVmomi.vim.ElementDescription):
   """
   Describes a user-defined option.
   
   The name of each option is identified by the
   \"key\" property, inherited from the `pyVmomi.vim.ElementDescription`
   data object type.
   You can indicate the property's position in a hierarchy by using a dot-separated
   notation. The string preceding the first dot is the top of the hierarchy. The
   hierarchy descends to a new sublevel with each dot.
   For example, \"Ethernet.NetworkConnection.Bridged\".
   
   Attributes:
       optionType: The option type which defines allowed values.
   """
   optionType: OptionType


class OptionManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed object type is used for managing key/value pair
   options.
   - You can define options on the fly only if the option is supported
     by the concrete implementation, in a logical tree using a dot notation
     for keys. For example, \"Ethernet.Connection\" describes the Connection
     option as child of the Ethernet option.
   - Options can be updated even if not visible in supportedOption or
     settings or the queryMethod returned values only if supported by the
     concrete implementation.
   - Attempt to add random Options that are not supported by the concrete
     implementation may result in unexpected side-effects.
   - You can use the queryMethod to retrieve a single property or
     a subset of properties based on the dot notation path.
   """
   @property
   def supportedOption(self) -> list[OptionDef]:
      """
      A list of supported key/value pair options including their
      type information.
      """
      ...
   @property
   def setting(self) -> list[OptionValue]:
      """A list of the current settings for the key/value pair options."""
      ...

   def QueryView(self, name: _typing.Optional[str]) -> list[OptionValue]:
      """
      Returns a specific node or nodes in the option hierarchy.
      
      This method might require any of the following privileges depending
      on where the property fits in the inventory tree.
      - System.View on the root folder, if this is used to read settings
        in the \"client\" subtree.
      - System.Read on the root folder, if this is used to read all settings
        or any settings beside those in the \"client\" subtree.
      - System.Read on the host, if this is used to read the advanced
        options for a host configuration.
      
      Returns:
          The option with the given name. If the name ends with a
          dot, all options for that subtree are returned.
      
      Raises:
          pyVmomi.vim.fault.InvalidName: if no option or subtree exists with the
              given name.
      """
      ...
   def UpdateValues(self, changedValue: list[OptionValue]) -> None:
      """
      Updates one or more options.
      
      The options are changed one by one, and the operation is not atomic.
      This means that on failure some of the options may not be changed.
      
      A nested option setting can be named using a dot notation; for example,
      system.cacheSize.
      
      This method might require any of the following privileges depending
      on where the property fits in the inventory tree.
      - Global.Settings on the root folder, if this is used to modify the
        settings in the service node.
      - Host.Config.AdvancedConfig on the host, if this is used to set the
        advanced options in the host configuration.
      
      Raises:
          pyVmomi.vim.fault.InvalidName: if one or more OptionValue objects refers to a
              non-existent option.
      """
      ...


class OptionValue(pyVmomi.vmodl.DynamicData):
   """
   Describes the key/value pair of a configured option.
   
   Attributes:
       key: The name of the option using dot notation to reflect the
           option's position in a hierarchy.
           
           For example, you might
           have an option called \"Ethernet\" and another option that is
           a child of that called \"Connection\". In this case, the key
           for the latter could be defined as \"Ethernet.Connection\"
       value: The value of the option.
           
           The Any data object type enables you to
           define any value for the option. Typically, however, the value
           of an option is of type String or Integer.
   """
   key: str
   value: _typing.Optional[object] = None


class StringOption(OptionType):
   """
   The StringOption data object type is used to define an open-ended
   string value based on an optional subset of valid characters.
   
   Attributes:
       defaultValue: The default value.
       validCharacters: The string containing the set of valid characters.
           
           If a string
           option is not specified, all strings are allowed.
   """
   defaultValue: str
   validCharacters: _typing.Optional[str] = None
