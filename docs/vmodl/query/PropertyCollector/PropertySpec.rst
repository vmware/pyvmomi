.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _pathSet: ../../../vmodl/query/PropertyCollector/PropertySpec.rst#pathSet

.. _PropertySpec: ../../../vmodl/query/PropertyCollector/PropertySpec.rst

.. _RetrieveResult: ../../../vmodl/query/PropertyCollector/RetrieveResult.rst

.. _PropertyCollector: ../../../vmodl/query/PropertyCollector.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _PropertyFilterSpec: ../../../vmodl/query/PropertyCollector/FilterSpec.rst


vmodl.query.PropertyCollector.PropertySpec
==========================================
  Within a `PropertyFilterSpec`_ , A `PropertySpec`_ specifies which properties should be reported to the client for objects of the given managed object type that are visited and not skipped. One more subtle side effect is that if a managed object is visited and not skipped, but there is no `PropertySpec`_ associated with the managed object's type, the managed object will not be reported to the client.Also, the set of properties applicable to a given managed object type is the union of the properties implied by the `PropertySpec`_ objects even, in the case of a `RetrieveResult`_ , where there may be an applicable `PropertySpec`_ in more than one filter.
:extends: vmodl.DynamicData_

Attributes:
    type (`str`_):

       Name of the managed object type being collected.
    all (`bool`_, optional):

       Specifies whether or not all properties of the object are read. If this property is set to true, the `pathSet`_ property is ignored.
    pathSet (`str`_, optional):

       Specifies which managed object properties are retrieved. If the `pathSet`_ is empty, then the `PropertyCollector`_ retrieves references to the managed objects and no managed object properties are collected.
