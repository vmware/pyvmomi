
vmodl.query.PropertyCollector.ObjectUpdate
==========================================
  The `ObjectUpdate <vmodl/query/PropertyCollector/ObjectUpdate.rst>`_ data object type contains information about changes to a particular managed object. We distinguish updates when an object is created, destroyed, or modified, as well as when the object enters or leaves the set of objects dynamically associated with a filter.
:extends: vmodl.DynamicData_

Attributes:
    kind (`vmodl.query.PropertyCollector.ObjectUpdate.Kind <vmodl/query/PropertyCollector/ObjectUpdate/Kind.rst>`_):

       Kind of update that caused the filter to report a change.
    obj (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_):

       Reference to the managed object to which this update applies.
    changeSet ([`vmodl.query.PropertyCollector.Change <vmodl/query/PropertyCollector/Change.rst>`_], optional):

       Optional set of changes to the object. Present only if the "kind" is either "modify" or "enter".
    missingSet ([`vmodl.query.PropertyCollector.MissingProperty <vmodl/query/PropertyCollector/MissingProperty.rst>`_], optional):

       Properties whose value could not be retrieved and their associated faults. Present only if the "kind" is either "modify" or "enter".
