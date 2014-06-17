.. _ObjectUpdate: ../../../vmodl/query/PropertyCollector/ObjectUpdate.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.ManagedObject: ../../../vim.ExtensibleManagedObject.rst

.. _vmodl.query.PropertyCollector.Change: ../../../vmodl/query/PropertyCollector/Change.rst

.. _vmodl.query.PropertyCollector.MissingProperty: ../../../vmodl/query/PropertyCollector/MissingProperty.rst

.. _vmodl.query.PropertyCollector.ObjectUpdate.Kind: ../../../vmodl/query/PropertyCollector/ObjectUpdate/Kind.rst


vmodl.query.PropertyCollector.ObjectUpdate
==========================================
  The `ObjectUpdate`_ data object type contains information about changes to a particular managed object. We distinguish updates when an object is created, destroyed, or modified, as well as when the object enters or leaves the set of objects dynamically associated with a filter.
:extends: vmodl.DynamicData_

Attributes:
    kind (`vmodl.query.PropertyCollector.ObjectUpdate.Kind`_):

       Kind of update that caused the filter to report a change.
    obj (`vmodl.ManagedObject`_):

       Reference to the managed object to which this update applies.
    changeSet (`vmodl.query.PropertyCollector.Change`_, optional):

       Optional set of changes to the object. Present only if the "kind" is either "modify" or "enter".
    missingSet (`vmodl.query.PropertyCollector.MissingProperty`_, optional):

       Properties whose value could not be retrieved and their associated faults. Present only if the "kind" is either "modify" or "enter".
