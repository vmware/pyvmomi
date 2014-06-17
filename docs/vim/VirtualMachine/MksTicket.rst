.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.VirtualMachine.MksTicket
============================
  This data object contains the information needed to establish an MKS (mouse-keyboard-screen) connection to a running virtual machine.
:extends: vmodl.DynamicData_
**deprecated**


Attributes:
    ticket (`str`_):

       The ticket name. This is used as the username and password for the MKS connection.
    cfgFile (`str`_):

       The name of the configuration file for the virtual machine.
    host (`str`_, optional):

       The host with which to establish a connection. If the host is not specified, it is assumed that the requesting entity knows the appropriate host with which to connect.
    port (`int`_, optional):

       The port number to use. If the port is not specified, it is assumed that the requesting entity knows the appropriate port to use when making a new connection.
    sslThumbprint (`str`_, optional):

       The expected thumbprint of the SSL cert of the host to which we are connecting.
