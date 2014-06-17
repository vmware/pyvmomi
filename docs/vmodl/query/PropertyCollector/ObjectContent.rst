.. _ObjectContent: ../../../vmodl/query/PropertyCollector/ObjectContent.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.ManagedObject: ../../../vim.ExtensibleManagedObject.rst

.. _vmodl.DynamicProperty: ../../../vmodl/DynamicProperty.rst

.. _vmodl.query.PropertyCollector.MissingProperty: ../../../vmodl/query/PropertyCollector/MissingProperty.rst


vmodl.query.PropertyCollector.ObjectContent
===========================================
  The `ObjectContent`_ data object type contains the contents retrieved for a single managed object.
:extends: vmodl.DynamicData_

Attributes:
    obj (`vmodl.ManagedObject`_):

       Reference to the managed object that contains properties of interest.
    propSet (`vmodl.DynamicProperty`_, optional):

       Set of name-value pairs for the properties of the managed object.
    missingSet (`vmodl.query.PropertyCollector.MissingProperty`_, optional):

       Properties for which values could not be retrieved and the associated fault.
