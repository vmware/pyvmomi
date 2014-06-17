.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _selectSet: ../../../vmodl/query/PropertyCollector/ObjectSpec.rst#selectSet

.. _ObjectSpec: ../../../vmodl/query/PropertyCollector/ObjectSpec.rst

.. _PropertySpec: ../../../vmodl/query/PropertyCollector/PropertySpec.rst

.. _SelectionSpec: ../../../vmodl/query/PropertyCollector/SelectionSpec.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _PropertyFilterSpec: ../../../vmodl/query/PropertyCollector/FilterSpec.rst

.. _vmodl.ManagedObject: ../../../vim.ExtensibleManagedObject.rst

.. _vmodl.query.PropertyCollector.SelectionSpec: ../../../vmodl/query/PropertyCollector/SelectionSpec.rst


vmodl.query.PropertyCollector.ObjectSpec
========================================
  Within a `PropertyFilterSpec`_ , the `ObjectSpec`_ data object type specifies the managed object at which the filter begins to collect the managed object references and properties specified by the associated `PropertySpec`_ set. If the "skip" property is present and set to true, then the filter does not check to see if the starting object's type matches any of the types listed in the associated sets of `PropertySpec`_ data objects.If the `selectSet`_ property is present, then this specifies additional objects to filter. These objects are defined by one or more `SelectionSpec`_ objects.
:extends: vmodl.DynamicData_

Attributes:
    obj (`vmodl.ManagedObject`_, privilege: System.View):

       Starting object.
    skip (`bool`_, optional):

       Flag to specify whether or not to report this managed object's properties. If the flag is true, the filter will not report this managed object's properties.
    selectSet (`vmodl.query.PropertyCollector.SelectionSpec`_, optional):

       Set of selections to specify additional objects to filter.
