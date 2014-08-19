
vmodl.query.PropertyCollector.FilterSpec
========================================
  Specify the property data that is included in a filter. A filter can specify part of a single managed object, or parts of multiple related managed objects in an inventory hierarchy - for example, to collect updates from all virtual machines in a given folder.
:extends: vmodl.DynamicData_

Attributes:
    propSet ([`vmodl.query.PropertyCollector.PropertySpec <vmodl/query/PropertyCollector/PropertySpec.rst>`_]):

       Set of properties to include in the filter, specified for each object type.
    objectSet ([`vmodl.query.PropertyCollector.ObjectSpec <vmodl/query/PropertyCollector/ObjectSpec.rst>`_]):

       Set of specifications that determine the objects to filter.
    reportMissingObjectsInResults (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Control how to report missing objects during filter creation.If false or unset and `objectSet <vmodl/query/PropertyCollector/FilterSpec.rst#objectSet>`_ refers to missing objects, filter creation will fail with a `ManagedObjectNotFound <vmodl/fault/ManagedObjectNotFound.rst>`_ fault.If true and `objectSet <vmodl/query/PropertyCollector/FilterSpec.rst#objectSet>`_ refers to missing objects, filter creation will not fail and missing objects will be reported via filter results. This is the recommended setting when `objectSet <vmodl/query/PropertyCollector/FilterSpec.rst#objectSet>`_ refers to transient objects.In an `UpdateSet <vmodl/query/PropertyCollector/UpdateSet.rst>`_ missing objects will appear in the `missingSet <vmodl/query/PropertyCollector/FilterUpdate.rst#missingSet>`_ field.In a `RetrieveResult <vmodl/query/PropertyCollector/RetrieveResult.rst>`_ missing objects will simply be omitted from the objects field.For a call to `RetrieveProperties <vmodl/query/PropertyCollector.rst#retrieveContents>`_ missing objects will simply be omitted from the results.
