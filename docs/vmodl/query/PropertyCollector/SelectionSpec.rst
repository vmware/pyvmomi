.. _str: https://docs.python.org/2/library/stdtypes.html

.. _SelectionSpec: ../../../vmodl/query/PropertyCollector/SelectionSpec.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vmodl.query.PropertyCollector.SelectionSpec
===========================================
  The `SelectionSpec`_ is the base type for data object types that specify what additional objects to filter. The base type contains only an optional "name" field, which allows a selection to be named for future reference. More information is available in the subtype.Named selections support recursive specifications on an object hierarchy. When used by a derived object, the "name" field allows other `SelectionSpec`_ objects to refer to the object by name. When used as the base type only, the "name" field indicates recursion to the derived object by name.Names are meaningful only within the same FilterSpec.
:extends: vmodl.DynamicData_

Attributes:
    name (`str`_, optional):

       Name of the selection specification.
