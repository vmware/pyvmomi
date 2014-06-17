.. _objectSet: ../../../vmodl/query/PropertyCollector/FilterSpec.rst#objectSet

.. _SystemError: ../../../vmodl/fault/SystemError.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.ManagedObject: ../../../vim.ExtensibleManagedObject.rst

.. _ManagedObjectNotFound: ../../../vmodl/fault/ManagedObjectNotFound.rst

.. _vmodl.LocalizedMethodFault: ../../../vmodl/LocalizedMethodFault.rst


vmodl.query.PropertyCollector.MissingObject
===========================================
  Used for reporting missing objects that were explicitly referenced by a filter spec. In other words, any of the objects referenced in `objectSet`_ 
:extends: vmodl.DynamicData_

Attributes:
    obj (`vmodl.ManagedObject`_):

       The object that is being reported missing
    fault (`vmodl.LocalizedMethodFault`_):

       Fault describing the failure to lookup this objectThe possible faults for missing objects are:
        * 
        * `SystemError`_
        * if there was some unknown problem looking up the object
        * 
        * `ManagedObjectNotFound`_
        * if the object is no longer available
        * 
