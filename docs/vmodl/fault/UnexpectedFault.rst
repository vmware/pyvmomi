
vmodl.fault.UnexpectedFault
===========================
    :extends:

        `vmodl.RuntimeFault <vmodl/RuntimeFault.rst>`_

  An UnexpectedFault may be thrown when a newer version of the server reports a error that a cannot be converted to a fault that a client that is using an older version of the API would expect.

Attributes:

    faultName (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    fault (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




