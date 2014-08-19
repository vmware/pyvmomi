
vmodl.query.PropertyCollector.FilterUpdate
==========================================
  The `PropertyFilterUpdate <vmodl/query/PropertyCollector/FilterUpdate.rst>`_ data object type contains a list of updates to data visible through a specific filter. Note that if a property changes through multiple filters, then a client receives an update for each filter.
:extends: vmodl.DynamicData_

Attributes:
    filter (`vmodl.query.PropertyCollector.Filter <vmodl/query/PropertyCollector/Filter.rst>`_):

       Filter that was updated.
    objectSet ([`vmodl.query.PropertyCollector.ObjectUpdate <vmodl/query/PropertyCollector/ObjectUpdate.rst>`_], optional):

       Set of changes to object properties in the filter.
    missingSet ([`vmodl.query.PropertyCollector.MissingObject <vmodl/query/PropertyCollector/MissingObject.rst>`_], optional):

       Objects that could not be found on the server, but were specified in a `objectSet <vmodl/query/PropertyCollector/FilterSpec.rst#objectSet>`_ .This field will only be populated for objects that were determined to be missing since the data version passed to `CheckForUpdates <vmodl/query/PropertyCollector.rst#checkForUpdates>`_ , `WaitForUpdates <vmodl/query/PropertyCollector.rst#waitForUpdates>`_ , or `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_ and will not contain objects that were missing prior to that data version.
