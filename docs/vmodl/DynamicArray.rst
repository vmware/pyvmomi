.. _str: https://docs.python.org/2/library/stdtypes.html

.. _object: https://docs.python.org/2/library/stdtypes.html


vmodl.DynamicArray
==================
  DynamicArray is a data object type that represents an array of dynamically-typed objects. A client should only see a DynamicArray object when the element type is unknown (meaning the type is newer than the client). Otherwise, a client would see the type as T[] where T is known.

Attributes:
    dynamicType (`str`_, optional):

       Reserved.
    val ([`object`_]):

       Array of dynamic values.
