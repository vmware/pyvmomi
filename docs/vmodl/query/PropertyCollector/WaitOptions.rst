.. _int: https://docs.python.org/2/library/stdtypes.html

.. _UpdateSet: ../../../vmodl/query/PropertyCollector/UpdateSet.rst

.. _truncated: ../../../vmodl/query/PropertyCollector/UpdateSet.rst#truncated

.. _ObjectUpdate: ../../../vmodl/query/PropertyCollector/ObjectUpdate.rst

.. _maxWaitSeconds: ../../../vmodl/query/PropertyCollector/WaitOptions.rst#maxWaitSeconds

.. _vSphere API 4.1: ../../../vim/version.rst#vmodlqueryversionversion3

.. _CheckForUpdates: ../../../vmodl/query/PropertyCollector.rst#checkForUpdates

.. _WaitForUpdatesEx: ../../../vmodl/query/PropertyCollector.rst#waitForUpdatesEx

.. _maxObjectUpdates: ../../../vmodl/query/PropertyCollector/WaitOptions.rst#maxObjectUpdates

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _PropertyCollector: ../../../vmodl/query/PropertyCollector.rst


vmodl.query.PropertyCollector.WaitOptions
=========================================
  Options for `WaitForUpdatesEx`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    maxWaitSeconds (`int`_, optional):

       The number of seconds the `PropertyCollector`_ should wait before returning null. Returning updates may take longer if the actual calculation time exceeds `maxWaitSeconds`_ . Additionally `PropertyCollector`_ policy may cause it to return null sooner than `maxWaitSeconds`_ .An unset value causes `WaitForUpdatesEx`_ to wait as long as possible for updates. Policy may still cause the `PropertyCollector`_ to return null at some point.A value of 0 causes `WaitForUpdatesEx`_ to do one update calculation and return any results. This behavior is similar to `CheckForUpdates`_ .A positive value causes `WaitForUpdatesEx`_ to return null if no updates are available within the specified number of seconds. The choice of a positive value often depends on the client communication stack. For example it may be helpful to choose a duration shorter than a local HTTP request timeout. Typically it should be no shorter than a few minutes.A negative value is illegal.
    maxObjectUpdates (`int`_, optional):

       The maximum number of `ObjectUpdate`_ entries that should be returned in a single result from `WaitForUpdatesEx`_ . See `truncated`_ An unset value indicates that there is no maximum. In this case `PropertyCollector`_ policy may still limit the number of objects that appear in an `UpdateSet`_ .A positive value causes `WaitForUpdatesEx`_ to suspend the update calculation when the total count of `ObjectUpdate`_ entries ready to return reaches the specified maximum. `PropertyCollector`_ policy may still limit the total count to something less than `maxObjectUpdates`_ .A value less than or equal to 0 is illegal.
