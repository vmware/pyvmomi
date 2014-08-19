
vmodl.query.PropertyCollector.RetrieveResult
============================================
  Result of `RetrievePropertiesEx <vmodl/query/PropertyCollector.rst#retrievePropertiesEx>`_ and `ContinueRetrievePropertiesEx <vmodl/query/PropertyCollector.rst#continueRetrievePropertiesEx>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vmodlqueryversionversion3>`_

Attributes:
    token (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       A token used to retrieve further retrieve results.If set, the token should be passed to `ContinueRetrievePropertiesEx <vmodl/query/PropertyCollector.rst#continueRetrievePropertiesEx>`_ to retrieve more results. Each token may be passed to continueRetrievePropertiesEx only once, and only in the same session in which it was returned and to the same `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ object that returned it.If unset, there are no further results to retrieve after this `RetrieveResult <vmodl/query/PropertyCollector/RetrieveResult.rst>`_ .
    objects ([`vmodl.query.PropertyCollector.ObjectContent <vmodl/query/PropertyCollector/ObjectContent.rst>`_]):

       retrieved objects.
