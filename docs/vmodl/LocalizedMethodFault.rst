
vmodl.LocalizedMethodFault
==========================
  A wrapper class used to pass MethodFault data objects over the wire along with a localized display message for the fault.
:extends: vmodl.DynamicData_

Attributes:
    fault (`vmodl.MethodFault <vmodl/MethodFault.rst>`_):

    localizedMessage (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The localized message that would be sent in the faultstring element of the SOAP Fault. It is optional so that clients are not required to send a localized message to the server, but servers are required to send the localized message to clients.
