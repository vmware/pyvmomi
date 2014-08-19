
vmodl.DynamicArray
==================
  DynamicArray is a data object type that represents an array of dynamically-typed objects. A client should only see a DynamicArray object when the element type is unknown (meaning the type is newer than the client). Otherwise, a client would see the type as T[] where T is known.

Attributes:
    dynamicType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Reserved.
    val ([`object <https://docs.python.org/2/library/stdtypes.html>`_]):

       Array of dynamic values.
