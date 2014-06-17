.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _UpdateSet: ../../../vmodl/query/PropertyCollector/UpdateSet.rst

.. _objectSet: ../../../vmodl/query/PropertyCollector/FilterSpec.rst#objectSet

.. _missingSet: ../../../vmodl/query/PropertyCollector/FilterUpdate.rst#missingSet

.. _RetrieveResult: ../../../vmodl/query/PropertyCollector/RetrieveResult.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _RetrieveProperties: ../../../vmodl/query/PropertyCollector.rst#retrieveContents

.. _ManagedObjectNotFound: ../../../vmodl/fault/ManagedObjectNotFound.rst

.. _vmodl.query.PropertyCollector.ObjectSpec: ../../../vmodl/query/PropertyCollector/ObjectSpec.rst

.. _vmodl.query.PropertyCollector.PropertySpec: ../../../vmodl/query/PropertyCollector/PropertySpec.rst


vmodl.query.PropertyCollector.FilterSpec
========================================
  Specify the property data that is included in a filter. A filter can specify part of a single managed object, or parts of multiple related managed objects in an inventory hierarchy - for example, to collect updates from all virtual machines in a given folder.
:extends: vmodl.DynamicData_

Attributes:
    propSet (`vmodl.query.PropertyCollector.PropertySpec`_):

       Set of properties to include in the filter, specified for each object type.
    objectSet (`vmodl.query.PropertyCollector.ObjectSpec`_):

       Set of specifications that determine the objects to filter.
    reportMissingObjectsInResults (`bool`_, optional):

       Control how to report missing objects during filter creation.If false or unset and `objectSet`_ refers to missing objects, filter creation will fail with a `ManagedObjectNotFound`_ fault.If true and `objectSet`_ refers to missing objects, filter creation will not fail and missing objects will be reported via filter results. This is the recommended setting when `objectSet`_ refers to transient objects.In an `UpdateSet`_ missing objects will appear in the `missingSet`_ field.In a `RetrieveResult`_ missing objects will simply be omitted from the objects field.For a call to `RetrieveProperties`_ missing objects will simply be omitted from the results.
