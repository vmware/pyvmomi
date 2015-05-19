.. _str: https://docs.python.org/2/library/stdtypes.html

.. _SystemError: ../../../vmodl/fault/SystemError.rst

.. _SecurityError: ../../../vmodl/fault/SecurityError.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../../vmodl/LocalizedMethodFault.rst


vmodl.query.PropertyCollector.MissingProperty
=============================================
  Used for reporting properties for which values could not be retrieved.
:extends: vmodl.DynamicData_

Attributes:
    path (`str`_):

       Property for which a value could not be retrieved
    fault (`vmodl.LocalizedMethodFault`_):

       Fault describing the failure to retrieve the property value.The possible faults for missing properties are:
        * 
        * `SystemError`_
        * if there was some unknown problem reading the value
        * 
        * `SecurityError`_
        * if the logged in session did not have permission to read the value
        * 
