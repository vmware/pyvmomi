
vim.dvs.PortConnectee
=====================
  Information about the entity that connects to a DistributedVirtualPort.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    connectedEntity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_, optional):

       The connected entity. This property should always be set unless the user's setting does not have System.Read privilege on the object referred to by this property.
    nicKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The key of the virtual NIC that connects to this port.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The type of the connectee. See `ConnecteeType <vim/dvs/PortConnectee/ConnecteeType.rst>`_ for valid values.
    addressHint (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       A hint on address information of the NIC that connects to this port.
