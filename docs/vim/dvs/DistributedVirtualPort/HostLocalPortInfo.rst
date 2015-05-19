.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.dvs.DistributedVirtualPort.Setting: ../../../vim/dvs/DistributedVirtualPort/Setting.rst


vim.dvs.DistributedVirtualPort.HostLocalPortInfo
================================================
  This data object type describes the information about the host local port. A host local port is created to resurrect the management network connection on a VMkernel Virtual NIC.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    switchUuid (`str`_):

       UUID of the vSphere Distributed Switch that management interface is connected to.
    portKey (`str`_):

       Portkey of the DVPort that management interface is now connected to.
    setting (`vim.dvs.DistributedVirtualPort.Setting`_):

       The configuration of the new host local port.
    vnic (`str`_):

       The Virtual NIC device connected to this port
