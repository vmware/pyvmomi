.. _objectSet: ../../../vmodl/query/PropertyCollector/FilterSpec.rst#objectSet

.. _WaitForUpdates: ../../../vmodl/query/PropertyCollector.rst#waitForUpdates

.. _CheckForUpdates: ../../../vmodl/query/PropertyCollector.rst#checkForUpdates

.. _WaitForUpdatesEx: ../../../vmodl/query/PropertyCollector.rst#waitForUpdatesEx

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _PropertyFilterUpdate: ../../../vmodl/query/PropertyCollector/FilterUpdate.rst

.. _vmodl.query.PropertyCollector.Filter: ../../../vmodl/query/PropertyCollector/Filter.rst

.. _vmodl.query.PropertyCollector.ObjectUpdate: ../../../vmodl/query/PropertyCollector/ObjectUpdate.rst

.. _vmodl.query.PropertyCollector.MissingObject: ../../../vmodl/query/PropertyCollector/MissingObject.rst


vmodl.query.PropertyCollector.FilterUpdate
==========================================
  The `PropertyFilterUpdate`_ data object type contains a list of updates to data visible through a specific filter. Note that if a property changes through multiple filters, then a client receives an update for each filter.
:extends: vmodl.DynamicData_

Attributes:
    filter (`vmodl.query.PropertyCollector.Filter`_):

       Filter that was updated.
    objectSet ([`vmodl.query.PropertyCollector.ObjectUpdate`_], optional):

       Set of changes to object properties in the filter.
    missingSet ([`vmodl.query.PropertyCollector.MissingObject`_], optional):

       Objects that could not be found on the server, but were specified in a `objectSet`_ .This field will only be populated for objects that were determined to be missing since the data version passed to `CheckForUpdates`_ , `WaitForUpdates`_ , or `WaitForUpdatesEx`_ and will not contain objects that were missing prior to that data version.
