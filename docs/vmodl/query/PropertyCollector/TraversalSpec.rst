.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _TraversalSpec: ../../../vmodl/query/PropertyCollector/TraversalSpec.rst

.. _vmodl.query.PropertyCollector.SelectionSpec: ../../../vmodl/query/PropertyCollector/SelectionSpec.rst


vmodl.query.PropertyCollector.TraversalSpec
===========================================
  The `TraversalSpec`_ data object type specifies how to derive a new set of objects to add to the filter.It specifies a property path whose value is either another managed object or an array of managed objects included in the set of objects for consideration. This data object can also be named, using the "name" field in the base type.
:extends: vmodl.query.PropertyCollector.SelectionSpec_

Attributes:
    type (`str`_):

       Name of the object type containing the property.
    path (`str`_):

       Name of the property to use in order to select additional objects.
    skip (`bool`_, optional):

       Flag to indicate whether or not to filter the object in the "path" field.
    selectSet (`vmodl.query.PropertyCollector.SelectionSpec`_, optional):

       Optional set of selections to specify additional objects to filter.
