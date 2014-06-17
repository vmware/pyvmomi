.. _vmodl.RuntimeFault: ../../vmodl/RuntimeFault.rst


vmodl.fault.InvalidRequest
==========================
    :extends:

        `vmodl.RuntimeFault`_

  An InvalidRequest fault is thrown in response to a malformed request to the server that fails in the transport layer, e.g., the SOAP XML request was invalid. Subtypes of this fault, provides more specific transport errors, such as a using a reference to an unknown managed object type or method.

Attributes:




