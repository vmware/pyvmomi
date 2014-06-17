.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicProperty: ../vmodl/DynamicProperty.rst


vmodl.DynamicData
=================
  DynamicData is a builtin object model data object type for manipulating data properties dynamically. The primary usage is as a base class for types that may be extended with subtypes in the future, where new properties should be sent to old clients as a set of dynamic properties.

Attributes:
    dynamicType (`str`_, optional):

       Reserved.
    dynamicProperty (`vmodl.DynamicProperty`_, optional):

       Set of dynamic properties. This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future.
