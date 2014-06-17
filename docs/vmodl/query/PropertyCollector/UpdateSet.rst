.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _UpdateSet: ../../../vmodl/query/PropertyCollector/UpdateSet.rst

.. _truncated: ../../../vmodl/query/PropertyCollector/UpdateSet.rst#truncated

.. _ObjectUpdate: ../../../vmodl/query/PropertyCollector/ObjectUpdate.rst

.. _WaitForUpdates: ../../../vmodl/query/PropertyCollector.rst#waitForUpdates

.. _CheckForUpdates: ../../../vmodl/query/PropertyCollector.rst#checkForUpdates

.. _WaitForUpdatesEx: ../../../vmodl/query/PropertyCollector.rst#waitForUpdatesEx

.. _maxObjectUpdates: ../../../vmodl/query/PropertyCollector/WaitOptions.rst#maxObjectUpdates

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _PropertyCollector: ../../../vmodl/query/PropertyCollector.rst

.. _PropertyFilterUpdate: ../../../vmodl/query/PropertyCollector/FilterUpdate.rst

.. _vmodl.query.PropertyCollector.FilterUpdate: ../../../vmodl/query/PropertyCollector/FilterUpdate.rst


vmodl.query.PropertyCollector.UpdateSet
=======================================
  A set of updates that represent the changes since a prior call to `CheckForUpdates`_ , `WaitForUpdates`_ , or `WaitForUpdatesEx`_ .
:extends: vmodl.DynamicData_

Attributes:
    version (`str`_):

       New data version to pass in the next call to `CheckForUpdates`_ , `WaitForUpdates`_ , or `WaitForUpdatesEx`_ . These versions, although they are opaque, are strongly ordered in the sense that passing a version to `WaitForUpdates`_ , `CheckForUpdates`_ or `WaitForUpdatesEx`_ requests updates that reflect changes in the objects selected by the Filter that happened after the specified version.
    filterSet (`vmodl.query.PropertyCollector.FilterUpdate`_, optional):

       Set of managed object updates detected by specific filters. Updates are reported in sets. Each set is associated with a reference to a filter that detected the updates in the set.
    truncated (`bool`_, optional):

       If true, this `UpdateSet`_ contains results from a suspended change calculation, which places restrictions on the use of version.The `PropertyCollector`_ may suspend a calculation due to server policy or if the total number of `ObjectUpdate`_ entries summed across every `PropertyFilterUpdate`_ reached the maximum specified in `maxObjectUpdates`_ . The client can pass the "truncated data version" to `WaitForUpdatesEx`_ to resume the update calculation, which will start on the filter where it left off. A truncated data version cannot be used more than once and may not be passed to `CheckForUpdates`_ or `WaitForUpdates`_ . `truncated`_ will never be true in an `UpdateSet`_ returned from `CheckForUpdates`_ or `WaitForUpdates`_ .If false, this `UpdateSet`_ contains a complete change calculation or the last part of a series of suspended change calculations. The version may be passed to `CheckForUpdates`_ , `WaitForUpdates`_ , or `WaitForUpdatesEx`_ more than once. Re-using a version allows a client to recover a change sequence after a transient failure on a previous call.
