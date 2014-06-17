.. _str: https://docs.python.org/2/library/stdtypes.html

.. _ConnecteeType: ../../vim/dvs/PortConnectee/ConnecteeType.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst


vim.dvs.PortConnectee
=====================
  Information about the entity that connects to a DistributedVirtualPort.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    connectedEntity (`vim.ManagedEntity`_, optional):

       The connected entity. This property should always be set unless the user's setting does not have System.Read privilege on the object referred to by this property.
    nicKey (`str`_, optional):

       The key of the virtual NIC that connects to this port.
    type (`str`_, optional):

       The type of the connectee. See `ConnecteeType`_ for valid values.
    addressHint (`str`_, optional):

       A hint on address information of the NIC that connects to this port.
