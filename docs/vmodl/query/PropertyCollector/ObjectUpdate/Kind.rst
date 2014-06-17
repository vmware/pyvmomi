.. _vmodl.query.PropertyCollector.ObjectUpdate: ../../../../vmodl/query/PropertyCollector/ObjectUpdate.rst

.. _vmodl.query.PropertyCollector.ObjectUpdate.Kind: ../../../../vmodl/query/PropertyCollector/ObjectUpdate/Kind.rst

vmodl.query.PropertyCollector.ObjectUpdate.Kind
===============================================
  Enumeration of different kinds of updates.
  :contained by: `vmodl.query.PropertyCollector.ObjectUpdate`_

  :type: `vmodl.query.PropertyCollector.ObjectUpdate.Kind`_

  :name: leave

values:
--------

leave
   A managed object left the set of objects visible to a filter. For instance, this can happen when a virtual machine is destroyed.

modify
   A property of the managed object changed its value.

enter
   A managed object became visible to a filter for the first time. For instance, this can happen if a virtual machine is added to a folder.
