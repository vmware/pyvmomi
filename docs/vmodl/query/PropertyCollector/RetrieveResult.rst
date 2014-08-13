.. _str: https://docs.python.org/2/library/stdtypes.html

.. _RetrieveResult: ../../../vmodl/query/PropertyCollector/RetrieveResult.rst

.. _vSphere API 4.1: ../../../vim/version.rst#vmodlqueryversionversion3

.. _PropertyCollector: ../../../vmodl/query/PropertyCollector.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _RetrievePropertiesEx: ../../../vmodl/query/PropertyCollector.rst#retrievePropertiesEx

.. _ContinueRetrievePropertiesEx: ../../../vmodl/query/PropertyCollector.rst#continueRetrievePropertiesEx

.. _vmodl.query.PropertyCollector.ObjectContent: ../../../vmodl/query/PropertyCollector/ObjectContent.rst


vmodl.query.PropertyCollector.RetrieveResult
============================================
  Result of `RetrievePropertiesEx`_ and `ContinueRetrievePropertiesEx`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    token (`str`_, optional):

       A token used to retrieve further retrieve results.If set, the token should be passed to `ContinueRetrievePropertiesEx`_ to retrieve more results. Each token may be passed to continueRetrievePropertiesEx only once, and only in the same session in which it was returned and to the same `PropertyCollector`_ object that returned it.If unset, there are no further results to retrieve after this `RetrieveResult`_ .
    objects ([`vmodl.query.PropertyCollector.ObjectContent`_]):

       retrieved objects.
