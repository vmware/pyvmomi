
vmodl.query.PropertyCollector.ObjectSpec
========================================
  Within a `PropertyFilterSpec <vmodl/query/PropertyCollector/FilterSpec.rst>`_ , the `ObjectSpec <vmodl/query/PropertyCollector/ObjectSpec.rst>`_ data object type specifies the managed object at which the filter begins to collect the managed object references and properties specified by the associated `PropertySpec <vmodl/query/PropertyCollector/PropertySpec.rst>`_ set. If the "skip" property is present and set to true, then the filter does not check to see if the starting object's type matches any of the types listed in the associated sets of `PropertySpec <vmodl/query/PropertyCollector/PropertySpec.rst>`_ data objects.If the `selectSet <vmodl/query/PropertyCollector/ObjectSpec.rst#selectSet>`_ property is present, then this specifies additional objects to filter. These objects are defined by one or more `SelectionSpec <vmodl/query/PropertyCollector/SelectionSpec.rst>`_ objects.
:extends: vmodl.DynamicData_

Attributes:
    obj (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_, privilege: System.View):

       Starting object.
    skip (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to specify whether or not to report this managed object's properties. If the flag is true, the filter will not report this managed object's properties.
    selectSet ([`vmodl.query.PropertyCollector.SelectionSpec <vmodl/query/PropertyCollector/SelectionSpec.rst>`_], optional):

       Set of selections to specify additional objects to filter.
