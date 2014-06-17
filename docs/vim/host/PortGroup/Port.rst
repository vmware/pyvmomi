.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _PortGroupConnecteeType: ../../../vim/host/PortGroup/PortConnecteeType.rst


vim.host.PortGroup.Port
=======================
  A Port data object type is a runtime representation of network connectivity between a network service or virtual machine and a virtual switch. This is different from a port group in that the port group represents the configuration aspects of the network connection. The Port object provides runtime statistics.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_, optional):

       The linkable identifier.
    mac (`str`_, optional):

       The Media Access Control (MAC) address of network service of the virtual machine connected on this port.
    type (`str`_):

       The type of component connected on this port. Must be one of the values of `PortGroupConnecteeType`_ .
