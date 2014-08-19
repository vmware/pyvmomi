
vmodl.query.PropertyCollector.RetrieveOptions
=============================================
  Options for `RetrievePropertiesEx <vmodl/query/PropertyCollector.rst#retrievePropertiesEx>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vmodlqueryversionversion3>`_

Attributes:
    maxObjects (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum number of `ObjectContent <vmodl/query/PropertyCollector/ObjectContent.rst>`_ data objects that should be returned in a single result from `RetrievePropertiesEx <vmodl/query/PropertyCollector.rst#retrievePropertiesEx>`_ .An unset value indicates that there is no maximum. In this case `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ policy may still limit the number of objects. Any remaining objects may be retrieved with `ContinueRetrievePropertiesEx <vmodl/query/PropertyCollector.rst#continueRetrievePropertiesEx>`_ .A positive value causes `RetrievePropertiesEx <vmodl/query/PropertyCollector.rst#retrievePropertiesEx>`_ to suspend the retrieval when the count of objects reaches the specified maximum. `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ policy may still limit the count to something less than `maxObjects <vmodl/query/PropertyCollector/RetrieveOptions.rst#maxObjects>`_ . Any remaining objects may be retrieved with `ContinueRetrievePropertiesEx <vmodl/query/PropertyCollector.rst#continueRetrievePropertiesEx>`_ .A value less than or equal to 0 is illegal.
