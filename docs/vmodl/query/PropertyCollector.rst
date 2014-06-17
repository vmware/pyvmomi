.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _truncated: ../../vmodl/query/PropertyCollector/UpdateSet.rst#truncated

.. _CreateFilter: ../../vmodl/query/PropertyCollector.rst#createFilter

.. _maxWaitSeconds: ../../vmodl/query/PropertyCollector/WaitOptions.rst#maxWaitSeconds

.. _PropertyFilter: ../../vmodl/query/PropertyCollector/Filter.rst

.. _WaitForUpdates: ../../vmodl/query/PropertyCollector.rst#waitForUpdates

.. _CheckForUpdates: ../../vmodl/query/PropertyCollector.rst#checkForUpdates

.. _vSphere API 4.1: ../../vim/version.rst#vmodlqueryversionversion3

.. _RequestCanceled: ../../vmodl/fault/RequestCanceled.rst

.. _WaitForUpdatesEx: ../../vmodl/query/PropertyCollector.rst#waitForUpdatesEx

.. _PropertyCollector: ../../vmodl/query/PropertyCollector.rst

.. _RetrievePropertiesEx: ../../vmodl/query/PropertyCollector.rst#retrievePropertiesEx

.. _CreatePropertyCollector: ../../vmodl/query/PropertyCollector.rst#createPropertyCollector

.. _vmodl.fault.InvalidType: ../../vmodl/fault/InvalidType.rst

.. _DestroyPropertyCollector: ../../vmodl/query/PropertyCollector.rst#destroy

.. _vmodl.fault.NotSupported: ../../vmodl/fault/NotSupported.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vmodl.fault.RequestCanceled: ../../vmodl/fault/RequestCanceled.rst

.. _vmodl.query.InvalidProperty: ../../vmodl/query/InvalidProperty.rst

.. _vmodl.query.PropertyCollector: ../../vmodl/query/PropertyCollector.rst

.. _vmodl.fault.ManagedObjectNotFound: ../../vmodl/fault/ManagedObjectNotFound.rst

.. _vmodl.query.InvalidCollectorVersion: ../../vmodl/query/InvalidCollectorVersion.rst

.. _vmodl.query.PropertyCollector.Filter: ../../vmodl/query/PropertyCollector/Filter.rst

.. _vmodl.query.PropertyCollector.UpdateSet: ../../vmodl/query/PropertyCollector/UpdateSet.rst

.. _vmodl.query.PropertyCollector.FilterSpec: ../../vmodl/query/PropertyCollector/FilterSpec.rst

.. _vmodl.query.PropertyCollector.WaitOptions: ../../vmodl/query/PropertyCollector/WaitOptions.rst

.. _vmodl.query.PropertyCollector.ObjectContent: ../../vmodl/query/PropertyCollector/ObjectContent.rst

.. _vmodl.query.PropertyCollector.RetrieveResult: ../../vmodl/query/PropertyCollector/RetrieveResult.rst

.. _vmodl.query.PropertyCollector.RetrieveOptions: ../../vmodl/query/PropertyCollector/RetrieveOptions.rst


vmodl.query.PropertyCollector
=============================
  The `PropertyCollector`_ managed object retrieves and detects changes to the properties of other managed objects. The `RetrievePropertiesEx`_ method provides one-time property retrieval. The `WaitForUpdatesEx`_ method provides incremental change detection and supports both polling and notification.For change detection a client creates one or more filters to specify the subset of managed objects in which the client is interested. Filters keep per-session state to track incremental changes. Because this state is per-session:
   * A session cannot share its
   * `PropertyCollector`_
   * filters with other sessions
   * two different clients can share the same session, and so can share the same filters, but this is not recommended
   * When a session terminates, the associated
   * `PropertyCollector`_
   * filters are automatically destroyed.
   * 




Attributes
----------
    filter (`vmodl.query.PropertyCollector.Filter`_):
      privilege: System.View
       The filters that this `PropertyCollector`_ uses to determine the list of properties for which it detects incremental changes.


Methods
-------


CreateFilter(spec, partialUpdates):
   Creates a new filter for the given set of managed objects.


  Privilege:
               System.View



  Args:
    spec (`vmodl.query.PropertyCollector.FilterSpec`_):
       The specifications for the filter.


    partialUpdates (`bool`_):
       Flag to specify whether a change to a nested property should report only the nested change or the entire specified property value. If the value is true, a change should report only the nested property. If the value is false, a change should report the enclosing property named in the filter.




  Returns:
    `vmodl.query.PropertyCollector.Filter`_:
         A reference to the new filter.

  Raises:

    `vmodl.query.InvalidProperty`_: 
       if "spec" has a property that is not defined on one of the objects.

    `vmodl.fault.InvalidArgument`_: 
       if any of the following is true:
        * "spec" is empty.
        * "spec" contains a selection with properties not defined on its type.
        * 

    `vmodl.fault.InvalidType`_: 
       if "spec" contains, directly or indirectly, a type name that does not refer to a known type.

    `vmodl.fault.ManagedObjectNotFound`_: 
       See `reportMissingObjectsInResults`_ .


RetrieveProperties(specSet):
   Retrieves the specified properties of the specified managed objects.This method is similar to creating the filters, receiving the property values, and destroying the filters. The main difference is that the output blends the results from all the filters and reports a given managed object at most once no matter how many filters apply.The filter creation step can throw all of the same faults as `CreateFilter`_ .


  Privilege:
               System.Anonymous



  Args:
    specSet (`vmodl.query.PropertyCollector.FilterSpec`_):
       Specifies the properties to retrieve.




  Returns:
    `vmodl.query.PropertyCollector.ObjectContent`_:
         The data contents of the specified objects.

  Raises:

    `vmodl.query.InvalidProperty`_: 
       See `CreateFilter`_ 

    `vmodl.fault.InvalidArgument`_: 
       See `CreateFilter`_ 

    `vmodl.fault.InvalidType`_: 
       See `CreateFilter`_ 

    `vmodl.fault.ManagedObjectNotFound`_: 
       See `CreateFilter`_ 


CheckForUpdates(version):
   Checks for updates on properties specified by the union of all current filters. If no updates are pending, this method returns null.


  Privilege:
               System.View



  Args:
    version (`str`_, optional):
       The data version currently known to the client. The value must be either
        * the special initial version (an empty string)
        * a data version returned from
        * `CheckForUpdates`_
        * or
        * `WaitForUpdates`_
        * by the same
        * `PropertyCollector`_
        * on the same session.
        * a non-truncated data version returned from
        * `WaitForUpdatesEx`_
        * by the same
        * `PropertyCollector`_
        * on the same session.
        * 




  Returns:
    `vmodl.query.PropertyCollector.UpdateSet`_:
         Changes since the passed in data version. If no updates are pending, then this method returns null.

  Raises:

    `vmodl.query.InvalidCollectorVersion`_: 
       if the data version does not meet the requirements above.

    `vmodl.fault.RequestCanceled`_: 
       if `CancelWaitForUpdates`_ has been called or the session was closed or the `PropertyCollector`_ was destroyed at some point after the call was received but before the update calculation was actually started


WaitForUpdates(version):
   Calculate the set of updates for each existing filter in the session, returning when at least one filter has updates.


  Privilege:
               System.View



  Args:
    version (`str`_, optional):
       The data version currently known to the client. The value must be either
        * the special initial version (an empty string)
        * a data version returned from
        * `CheckForUpdates`_
        * or
        * `WaitForUpdates`_
        * by the same
        * `PropertyCollector`_
        * on the same session
        * a non-truncated data version returned from
        * `WaitForUpdatesEx`_
        * by the same
        * `PropertyCollector`_
        * on the same session.
        * 




  Returns:
    `vmodl.query.PropertyCollector.UpdateSet`_:
         Changes since the passed in data version.

  Raises:

    `vmodl.query.InvalidCollectorVersion`_: 
       if the data version does not meet the requirements above.

    `vmodl.fault.RequestCanceled`_: 
       if `CancelWaitForUpdates`_ has been called or the session was closed or the `PropertyCollector`_ was destroyed at some point after the call was received


CancelWaitForUpdates():
   Attempts to cancel outstanding calls to `WaitForUpdates`_ or `WaitForUpdatesEx`_ in the current session. If an update calculation is in process this method has no effect. If an update calculation is not in process any waiting calls complete quickly and report a `RequestCanceled`_ fault.


  Privilege:
               System.View



  Args:


  Returns:
    None
         


WaitForUpdatesEx(version, options):
   Calculate the set of updates for each existing filter in the session. `WaitForUpdatesEx`_ may return only partial update calculations. See `truncated`_ for a more detailed explanation. `WaitForUpdatesEx`_ may also return null after a timeout, either as requested by `maxWaitSeconds`_ or due to `PropertyCollector`_ policy.If an application uses waitForUpdatesEx it is strongly recommended that it not make concurrent calls to `WaitForUpdates`_ , `CheckForUpdates`_ , or `WaitForUpdatesEx`_ in the same session. Concurrent calls may cause suspended change calculations to be discarded.
  since: `vSphere API 4.1`_


  Privilege:
               System.View



  Args:
    version (`str`_, optional):
       The data version currently known to the client. The value must be either
        * the special initial data version (an empty string),
        * a data version returned from
        * `CheckForUpdates`_
        * or
        * `WaitForUpdates`_
        * 
        * a non-truncated data version returned from
        * `WaitForUpdatesEx`_
        * 
        * a truncated data version returned from the last call to
        * `WaitForUpdatesEx`_
        * with no intervening calls to
        * `WaitForUpdates`_
        * or
        * `CheckForUpdates`_
        * .
        * 


    options (`vmodl.query.PropertyCollector.WaitOptions`_, optional):
       Additional options controlling the change calculation. If omitted, equivalent to an options argument with no fields set.




  Returns:
    `vmodl.query.PropertyCollector.UpdateSet`_:
         Changes since the passed in version or null if there are no changes.

  Raises:

    `vmodl.query.InvalidCollectorVersion`_: 
       if the data version does not meet the requirements above.

    `vmodl.fault.RequestCanceled`_: 
       if `CancelWaitForUpdates`_ has been called or the session was closed or the `PropertyCollector`_ was destroyed at some point after the call was received


RetrievePropertiesEx(specSet, options):
   Retrieves the specified properties of the specified managed objects.This method is similar to creating the filters, receiving the property values, and destroying the filters. The main difference is that the output blends the results from all the filters and reports a given managed object at most once no matter how many filters apply.The filter creation step can throw all of the same faults as `CreateFilter`_ .
  since: `vSphere API 4.1`_


  Privilege:
               System.Anonymous



  Args:
    specSet (`vmodl.query.PropertyCollector.FilterSpec`_):
       Specifies the properties to retrieve.


    options (`vmodl.query.PropertyCollector.RetrieveOptions`_):
       Additional method options. If omitted, equivalent to an options argument with no fields set.




  Returns:
    `vmodl.query.PropertyCollector.RetrieveResult`_:
         retrieved objects or null if there are no matching objects.

  Raises:

    `vmodl.query.InvalidProperty`_: 
       See `CreateFilter`_ 

    `vmodl.fault.InvalidArgument`_: 
       if any of the following is true: See `CreateFilter`_ 

    `vmodl.fault.InvalidType`_: 
       See `CreateFilter`_ 

    `vmodl.fault.ManagedObjectNotFound`_: 
       See `CreateFilter`_ 


ContinueRetrievePropertiesEx(token):
   Retrieves additional results from a retrieval started by `RetrievePropertiesEx`_ on the same session on the same `PropertyCollector`_ .
  since: `vSphere API 4.1`_


  Privilege:
               System.Anonymous



  Args:
    token (`str`_):
       the token returned in the previous `RetrieveResult`_ returned on the same session by the same `PropertyCollector`_ .




  Returns:
    `vmodl.query.PropertyCollector.RetrieveResult`_:
         retrieved objects.

  Raises:

    `vmodl.query.InvalidProperty`_: 
       vmodl.query.InvalidProperty

    `vmodl.fault.InvalidArgument`_: 
       If the token does not match the token from the previous `RetrieveResult`_ returned on the same session by the same `PropertyCollector`_ .


CancelRetrievePropertiesEx(token):
   Discards remaining results from a retrieval started by `RetrievePropertiesEx`_ on the same session on the same `PropertyCollector`_ .
  since: `vSphere API 4.1`_


  Privilege:
               System.Anonymous



  Args:
    token (`str`_):
       the token returned in the previous `RetrieveResult`_ returned on the same session by the same `PropertyCollector`_ .




  Returns:
    None
         

  Raises:

    `vmodl.query.InvalidProperty`_: 
       vmodl.query.InvalidProperty

    `vmodl.fault.InvalidArgument`_: 
       If the token does not match the token from the previous `RetrieveResult`_ returned on the same session by the same `PropertyCollector`_ .


CreatePropertyCollector():
   Creates a new session-specific `PropertyCollector`_ that can be used to retrieve property updates independent of any other `PropertyCollector`_ . The newly created `PropertyCollector`_ is not tied to the creating `PropertyCollector`_ in any way and exists until it is destroyed by a call to `DestroyPropertyCollector`_ or until the session on which the PropertyCollector was created is closed. This is in contrast to the default `PropertyCollector`_ , which always exists, but still has session-specific data such as filters and unfinished update calculations that are discarded when the associated session is closed.A new `PropertyCollector`_ can be useful when multiple modules or even multiple clients that share the same session need to create their own `PropertyFilter`_ objects and process updates independently. They may also be useful to allow important updates to be seen on one `PropertyCollector`_ while a large update is being calculated on another. The underlying issue that this addresses is that any call to `WaitForUpdates`_ , `CheckForUpdates`_ , or `WaitForUpdatesEx`_ does updates on all the filters created on a given `PropertyCollector`_ on a given session.A more subtle use of multiple `PropertyCollector`_ objects is implied by the fact that the returned version value for the various updates calculations is strongly ordered. The only way this can make sense is that two different versions calculated on the same `PropertyCollector`_ on the same session cannot ever be created in parallel. This means that multiple calls to `WaitForUpdates`_ , `CheckForUpdates`_ , or `WaitForUpdatesEx`_ made to the same `PropertyCollector`_ on the same session on different threads of the same client, or even on different clients that share the same session are still handled on the server serially. Use of different `PropertyCollector`_ instances allows the server to handle these calculations in parallel.Typically a service that supports the `PropertyCollector`_ managed object type will automatically create a default `PropertyCollector`_ and provide some way to obtain a reference to this `PropertyCollector`_ . If not, it will have to provide some service-specific way to create the a `PropertyCollector`_ .
  since: `vSphere API 4.1`_


  Privilege:
               System.View



  Args:


  Returns:
    `vmodl.query.PropertyCollector`_:
         A reference to the new `PropertyCollector`_ .


DestroyPropertyCollector():
   Destroys this `PropertyCollector`_ .A `PropertyCollector`_ that was created by `CreatePropertyCollector`_ is automatically destroyed when the session on which it was created is closed. This method can be used to destroy them explicitly.An automatically created `PropertyCollector`_ provided by a service is not session specific and may not be destroyed.
  since: `vSphere API 4.1`_


  Privilege:
               System.View



  Args:


  Returns:
    None
         

  Raises:

    `vmodl.fault.NotSupported`_: 
       if this `PropertyCollector`_ is not allowed to be destroyed.


