
vmodl.query.PropertyCollector.MissingObject
===========================================
  Used for reporting missing objects that were explicitly referenced by a filter spec. In other words, any of the objects referenced in `objectSet <vmodl/query/PropertyCollector/FilterSpec.rst#objectSet>`_ 
:extends: vmodl.DynamicData_

Attributes:
    obj (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_):

       The object that is being reported missing
    fault (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       Fault describing the failure to lookup this objectThe possible faults for missing objects are:
        * 
        * `SystemError <vmodl/fault/SystemError.rst>`_
        * if there was some unknown problem looking up the object
        * 
        * `ManagedObjectNotFound <vmodl/fault/ManagedObjectNotFound.rst>`_
        * if the object is no longer available
        * 
