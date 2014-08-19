
vmodl.query.PropertyCollector.MissingProperty
=============================================
  Used for reporting properties for which values could not be retrieved.
:extends: vmodl.DynamicData_

Attributes:
    path (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Property for which a value could not be retrieved
    fault (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       Fault describing the failure to retrieve the property value.The possible faults for missing properties are:
        * 
        * `SystemError <vmodl/fault/SystemError.rst>`_
        * if there was some unknown problem reading the value
        * 
        * `SecurityError <vmodl/fault/SecurityError.rst>`_
        * if the logged in session did not have permission to read the value
        * 
