
vmodl.query.PropertyCollector
=============================
  The `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ managed object retrieves and detects changes to the properties of other managed objects. The `RetrievePropertiesEx <vmodl/query/PropertyCollector.rst#retrievePropertiesEx>`_ method provides one-time property retrieval. The `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_ method provides incremental change detection and supports both polling and notification.For change detection a client creates one or more filters to specify the subset of managed objects in which the client is interested. Filters keep per-session state to track incremental changes. Because this state is per-session:
   * A session cannot share its
   * `PropertyCollector <vmodl/query/PropertyCollector.rst>`_
   * filters with other sessions
   * two different clients can share the same session, and so can share the same filters, but this is not recommended
   * When a session terminates, the associated
   * `PropertyCollector <vmodl/query/PropertyCollector.rst>`_
   * filters are automatically destroyed.
   * 




Attributes
----------
    filter ([`vmodl.query.PropertyCollector.Filter <vmodl/query/PropertyCollector/Filter.rst>`_]):
      privilege: System.View
       The filters that this `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ uses to determine the list of properties for which it detects incremental changes.


Methods
-------


CreateFilter(spec, partialUpdates):
   Creates a new filter for the given set of managed objects.


  Privilege:
               System.View



  Args:
    spec (`vmodl.query.PropertyCollector.FilterSpec <vmodl/query/PropertyCollector/FilterSpec.rst>`_):
       The specifications for the filter.


    partialUpdates (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       Flag to specify whether a change to a nested property should report only the nested change or the entire specified property value. If the value is true, a change should report only the nested property. If the value is false, a change should report the enclosing property named in the filter.




  Returns:
    `vmodl.query.PropertyCollector.Filter <vmodl/query/PropertyCollector/Filter.rst>`_:
         A reference to the new filter.

  Raises:

    `vmodl.query.InvalidProperty <vmodl/query/InvalidProperty.rst>`_: 
       if "spec" has a property that is not defined on one of the objects.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if any of the following is true:
        * "spec" is empty.
        * "spec" contains a selection with properties not defined on its type.
        * 

    `vmodl.fault.InvalidType <vmodl/fault/InvalidType.rst>`_: 
       if "spec" contains, directly or indirectly, a type name that does not refer to a known type.

    `vmodl.fault.ManagedObjectNotFound <vmodl/fault/ManagedObjectNotFound.rst>`_: 
       See `reportMissingObjectsInResults <vmodl/query/PropertyCollector/FilterSpec.rst#reportMissingObjectsInResults>`_ .


RetrieveProperties(specSet):
   Retrieves the specified properties of the specified managed objects.This method is similar to creating the filters, receiving the property values, and destroying the filters. The main difference is that the output blends the results from all the filters and reports a given managed object at most once no matter how many filters apply.The filter creation step can throw all of the same faults as `CreateFilter <vmodl/query/PropertyCollector.rst#createFilter>`_ .


  Privilege:
               System.Anonymous



  Args:
    specSet (`vmodl.query.PropertyCollector.FilterSpec <vmodl/query/PropertyCollector/FilterSpec.rst>`_):
       Specifies the properties to retrieve.




  Returns:
    [`vmodl.query.PropertyCollector.ObjectContent <vmodl/query/PropertyCollector/ObjectContent.rst>`_]:
         The data contents of the specified objects.

  Raises:

    `vmodl.query.InvalidProperty <vmodl/query/InvalidProperty.rst>`_: 
       See `CreateFilter <vmodl/query/PropertyCollector.rst#createFilter>`_ 

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       See `CreateFilter <vmodl/query/PropertyCollector.rst#createFilter>`_ 

    `vmodl.fault.InvalidType <vmodl/fault/InvalidType.rst>`_: 
       See `CreateFilter <vmodl/query/PropertyCollector.rst#createFilter>`_ 

    `vmodl.fault.ManagedObjectNotFound <vmodl/fault/ManagedObjectNotFound.rst>`_: 
       See `CreateFilter <vmodl/query/PropertyCollector.rst#createFilter>`_ 


CheckForUpdates(version):
   Checks for updates on properties specified by the union of all current filters. If no updates are pending, this method returns null.


  Privilege:
               System.View



  Args:
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The data version currently known to the client. The value must be either
        * the special initial version (an empty string)
        * a data version returned from
        * `CheckForUpdates <vmodl/query/PropertyCollector.rst#checkForUpdates>`_
        * or
        * `WaitForUpdates <vmodl/query/PropertyCollector.rst#waitForUpdates>`_
        * by the same
        * `PropertyCollector <vmodl/query/PropertyCollector.rst>`_
        * on the same session.
        * a non-truncated data version returned from
        * `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_
        * by the same
        * `PropertyCollector <vmodl/query/PropertyCollector.rst>`_
        * on the same session.
        * 




  Returns:
    `vmodl.query.PropertyCollector.UpdateSet <vmodl/query/PropertyCollector/UpdateSet.rst>`_:
         Changes since the passed in data version. If no updates are pending, then this method returns null.

  Raises:

    `vmodl.query.InvalidCollectorVersion <vmodl/query/InvalidCollectorVersion.rst>`_: 
       if the data version does not meet the requirements above.

    `vmodl.fault.RequestCanceled <vmodl/fault/RequestCanceled.rst>`_: 
       if `CancelWaitForUpdates <vmodl/query/PropertyCollector.rst#cancelWaitForUpdates>`_ has been called or the session was closed or the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ was destroyed at some point after the call was received but before the update calculation was actually started


WaitForUpdates(version):
   Calculate the set of updates for each existing filter in the session, returning when at least one filter has updates.


  Privilege:
               System.View



  Args:
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The data version currently known to the client. The value must be either
        * the special initial version (an empty string)
        * a data version returned from
        * `CheckForUpdates <vmodl/query/PropertyCollector.rst#checkForUpdates>`_
        * or
        * `WaitForUpdates <vmodl/query/PropertyCollector.rst#waitForUpdates>`_
        * by the same
        * `PropertyCollector <vmodl/query/PropertyCollector.rst>`_
        * on the same session
        * a non-truncated data version returned from
        * `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_
        * by the same
        * `PropertyCollector <vmodl/query/PropertyCollector.rst>`_
        * on the same session.
        * 




  Returns:
    `vmodl.query.PropertyCollector.UpdateSet <vmodl/query/PropertyCollector/UpdateSet.rst>`_:
         Changes since the passed in data version.

  Raises:

    `vmodl.query.InvalidCollectorVersion <vmodl/query/InvalidCollectorVersion.rst>`_: 
       if the data version does not meet the requirements above.

    `vmodl.fault.RequestCanceled <vmodl/fault/RequestCanceled.rst>`_: 
       if `CancelWaitForUpdates <vmodl/query/PropertyCollector.rst#cancelWaitForUpdates>`_ has been called or the session was closed or the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ was destroyed at some point after the call was received


CancelWaitForUpdates():
   Attempts to cancel outstanding calls to `WaitForUpdates <vmodl/query/PropertyCollector.rst#waitForUpdates>`_ or `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_ in the current session. If an update calculation is in process this method has no effect. If an update calculation is not in process any waiting calls complete quickly and report a `RequestCanceled <vmodl/fault/RequestCanceled.rst>`_ fault.


  Privilege:
               System.View



  Args:


  Returns:
    None
         


WaitForUpdatesEx(version, options):
   Calculate the set of updates for each existing filter in the session. `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_ may return only partial update calculations. See `truncated <vmodl/query/PropertyCollector/UpdateSet.rst#truncated>`_ for a more detailed explanation. `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_ may also return null after a timeout, either as requested by `maxWaitSeconds <vmodl/query/PropertyCollector/WaitOptions.rst#maxWaitSeconds>`_ or due to `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ policy.If an application uses waitForUpdatesEx it is strongly recommended that it not make concurrent calls to `WaitForUpdates <vmodl/query/PropertyCollector.rst#waitForUpdates>`_ , `CheckForUpdates <vmodl/query/PropertyCollector.rst#checkForUpdates>`_ , or `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_ in the same session. Concurrent calls may cause suspended change calculations to be discarded.
  since: `vSphere API 4.1 <vim/version.rst#vmodlqueryversionversion3>`_


  Privilege:
               System.View



  Args:
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The data version currently known to the client. The value must be either
        * the special initial data version (an empty string),
        * a data version returned from
        * `CheckForUpdates <vmodl/query/PropertyCollector.rst#checkForUpdates>`_
        * or
        * `WaitForUpdates <vmodl/query/PropertyCollector.rst#waitForUpdates>`_
        * 
        * a non-truncated data version returned from
        * `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_
        * 
        * a truncated data version returned from the last call to
        * `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_
        * with no intervening calls to
        * `WaitForUpdates <vmodl/query/PropertyCollector.rst#waitForUpdates>`_
        * or
        * `CheckForUpdates <vmodl/query/PropertyCollector.rst#checkForUpdates>`_
        * .
        * 


    options (`vmodl.query.PropertyCollector.WaitOptions <vmodl/query/PropertyCollector/WaitOptions.rst>`_, optional):
       Additional options controlling the change calculation. If omitted, equivalent to an options argument with no fields set.




  Returns:
    `vmodl.query.PropertyCollector.UpdateSet <vmodl/query/PropertyCollector/UpdateSet.rst>`_:
         Changes since the passed in version or null if there are no changes.

  Raises:

    `vmodl.query.InvalidCollectorVersion <vmodl/query/InvalidCollectorVersion.rst>`_: 
       if the data version does not meet the requirements above.

    `vmodl.fault.RequestCanceled <vmodl/fault/RequestCanceled.rst>`_: 
       if `CancelWaitForUpdates <vmodl/query/PropertyCollector.rst#cancelWaitForUpdates>`_ has been called or the session was closed or the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ was destroyed at some point after the call was received


RetrievePropertiesEx(specSet, options):
   Retrieves the specified properties of the specified managed objects.This method is similar to creating the filters, receiving the property values, and destroying the filters. The main difference is that the output blends the results from all the filters and reports a given managed object at most once no matter how many filters apply.The filter creation step can throw all of the same faults as `CreateFilter <vmodl/query/PropertyCollector.rst#createFilter>`_ .
  since: `vSphere API 4.1 <vim/version.rst#vmodlqueryversionversion3>`_


  Privilege:
               System.Anonymous



  Args:
    specSet (`vmodl.query.PropertyCollector.FilterSpec <vmodl/query/PropertyCollector/FilterSpec.rst>`_):
       Specifies the properties to retrieve.


    options (`vmodl.query.PropertyCollector.RetrieveOptions <vmodl/query/PropertyCollector/RetrieveOptions.rst>`_):
       Additional method options. If omitted, equivalent to an options argument with no fields set.




  Returns:
    `vmodl.query.PropertyCollector.RetrieveResult <vmodl/query/PropertyCollector/RetrieveResult.rst>`_:
         retrieved objects or null if there are no matching objects.

  Raises:

    `vmodl.query.InvalidProperty <vmodl/query/InvalidProperty.rst>`_: 
       See `CreateFilter <vmodl/query/PropertyCollector.rst#createFilter>`_ 

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if any of the following is true: See `CreateFilter <vmodl/query/PropertyCollector.rst#createFilter>`_ 

    `vmodl.fault.InvalidType <vmodl/fault/InvalidType.rst>`_: 
       See `CreateFilter <vmodl/query/PropertyCollector.rst#createFilter>`_ 

    `vmodl.fault.ManagedObjectNotFound <vmodl/fault/ManagedObjectNotFound.rst>`_: 
       See `CreateFilter <vmodl/query/PropertyCollector.rst#createFilter>`_ 


ContinueRetrievePropertiesEx(token):
   Retrieves additional results from a retrieval started by `RetrievePropertiesEx <vmodl/query/PropertyCollector.rst#retrievePropertiesEx>`_ on the same session on the same `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ .
  since: `vSphere API 4.1 <vim/version.rst#vmodlqueryversionversion3>`_


  Privilege:
               System.Anonymous



  Args:
    token (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       the token returned in the previous `RetrieveResult <vmodl/query/PropertyCollector/RetrieveResult.rst>`_ returned on the same session by the same `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ .




  Returns:
    `vmodl.query.PropertyCollector.RetrieveResult <vmodl/query/PropertyCollector/RetrieveResult.rst>`_:
         retrieved objects.

  Raises:

    `vmodl.query.InvalidProperty <vmodl/query/InvalidProperty.rst>`_: 
       vmodl.query.InvalidProperty

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If the token does not match the token from the previous `RetrieveResult <vmodl/query/PropertyCollector/RetrieveResult.rst>`_ returned on the same session by the same `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ .


CancelRetrievePropertiesEx(token):
   Discards remaining results from a retrieval started by `RetrievePropertiesEx <vmodl/query/PropertyCollector.rst#retrievePropertiesEx>`_ on the same session on the same `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ .
  since: `vSphere API 4.1 <vim/version.rst#vmodlqueryversionversion3>`_


  Privilege:
               System.Anonymous



  Args:
    token (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       the token returned in the previous `RetrieveResult <vmodl/query/PropertyCollector/RetrieveResult.rst>`_ returned on the same session by the same `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ .




  Returns:
    None
         

  Raises:

    `vmodl.query.InvalidProperty <vmodl/query/InvalidProperty.rst>`_: 
       vmodl.query.InvalidProperty

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If the token does not match the token from the previous `RetrieveResult <vmodl/query/PropertyCollector/RetrieveResult.rst>`_ returned on the same session by the same `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ .


CreatePropertyCollector():
   Creates a new session-specific `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ that can be used to retrieve property updates independent of any other `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ . The newly created `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ is not tied to the creating `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ in any way and exists until it is destroyed by a call to `DestroyPropertyCollector <vmodl/query/PropertyCollector.rst#destroy>`_ or until the session on which the PropertyCollector was created is closed. This is in contrast to the default `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ , which always exists, but still has session-specific data such as filters and unfinished update calculations that are discarded when the associated session is closed.A new `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ can be useful when multiple modules or even multiple clients that share the same session need to create their own `PropertyFilter <vmodl/query/PropertyCollector/Filter.rst>`_ objects and process updates independently. They may also be useful to allow important updates to be seen on one `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ while a large update is being calculated on another. The underlying issue that this addresses is that any call to `WaitForUpdates <vmodl/query/PropertyCollector.rst#waitForUpdates>`_ , `CheckForUpdates <vmodl/query/PropertyCollector.rst#checkForUpdates>`_ , or `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_ does updates on all the filters created on a given `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ on a given session.A more subtle use of multiple `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ objects is implied by the fact that the returned version value for the various updates calculations is strongly ordered. The only way this can make sense is that two different versions calculated on the same `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ on the same session cannot ever be created in parallel. This means that multiple calls to `WaitForUpdates <vmodl/query/PropertyCollector.rst#waitForUpdates>`_ , `CheckForUpdates <vmodl/query/PropertyCollector.rst#checkForUpdates>`_ , or `WaitForUpdatesEx <vmodl/query/PropertyCollector.rst#waitForUpdatesEx>`_ made to the same `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ on the same session on different threads of the same client, or even on different clients that share the same session are still handled on the server serially. Use of different `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ instances allows the server to handle these calculations in parallel.Typically a service that supports the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ managed object type will automatically create a default `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ and provide some way to obtain a reference to this `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ . If not, it will have to provide some service-specific way to create the a `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ .
  since: `vSphere API 4.1 <vim/version.rst#vmodlqueryversionversion3>`_


  Privilege:
               System.View



  Args:


  Returns:
    `vmodl.query.PropertyCollector <vmodl/query/PropertyCollector.rst>`_:
         A reference to the new `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ .


DestroyPropertyCollector():
   Destroys this `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ .A `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ that was created by `CreatePropertyCollector <vmodl/query/PropertyCollector.rst#createPropertyCollector>`_ is automatically destroyed when the session on which it was created is closed. This method can be used to destroy them explicitly.An automatically created `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ provided by a service is not session specific and may not be destroyed.
  since: `vSphere API 4.1 <vim/version.rst#vmodlqueryversionversion3>`_


  Privilege:
               System.View



  Args:


  Returns:
    None
         

  Raises:

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if this `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ is not allowed to be destroyed.


