.. _int: https://docs.python.org/2/library/stdtypes.html

.. _maxObjects: ../../../vmodl/query/PropertyCollector/RetrieveOptions.rst#maxObjects

.. _ObjectContent: ../../../vmodl/query/PropertyCollector/ObjectContent.rst

.. _vSphere API 4.1: ../../../vim/version.rst#vmodlqueryversionversion3

.. _PropertyCollector: ../../../vmodl/query/PropertyCollector.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _RetrievePropertiesEx: ../../../vmodl/query/PropertyCollector.rst#retrievePropertiesEx

.. _ContinueRetrievePropertiesEx: ../../../vmodl/query/PropertyCollector.rst#continueRetrievePropertiesEx


vmodl.query.PropertyCollector.RetrieveOptions
=============================================
  Options for `RetrievePropertiesEx`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    maxObjects (`int`_, optional):

       The maximum number of `ObjectContent`_ data objects that should be returned in a single result from `RetrievePropertiesEx`_ .An unset value indicates that there is no maximum. In this case `PropertyCollector`_ policy may still limit the number of objects. Any remaining objects may be retrieved with `ContinueRetrievePropertiesEx`_ .A positive value causes `RetrievePropertiesEx`_ to suspend the retrieval when the count of objects reaches the specified maximum. `PropertyCollector`_ policy may still limit the count to something less than `maxObjects`_ . Any remaining objects may be retrieved with `ContinueRetrievePropertiesEx`_ .A value less than or equal to 0 is illegal.
