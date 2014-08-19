
vmodl.query.PropertyCollector.ObjectContent
===========================================
  The `ObjectContent <vmodl/query/PropertyCollector/ObjectContent.rst>`_ data object type contains the contents retrieved for a single managed object.
:extends: vmodl.DynamicData_

Attributes:
    obj (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_):

       Reference to the managed object that contains properties of interest.
    propSet ([`vmodl.DynamicProperty <vmodl/DynamicProperty.rst>`_], optional):

       Set of name-value pairs for the properties of the managed object.
    missingSet ([`vmodl.query.PropertyCollector.MissingProperty <vmodl/query/PropertyCollector/MissingProperty.rst>`_], optional):

       Properties for which values could not be retrieved and the associated fault.
