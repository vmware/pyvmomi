.. _str: https://docs.python.org/2/library/stdtypes.html

.. _device: ../../../vim/host/VirtualNic.rst#device

.. _HostVirtualNic: ../../../vim/host/VirtualNic.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostVirtualNicConfig: ../../../vim/host/VirtualNic/Config.rst

.. _DistributedVirtualSwitch: ../../../vim/DistributedVirtualSwitch.rst

.. _HostConfigChangeOperation: ../../../vim/host/ConfigChange/Operation.rst

.. _vim.host.VirtualNic.Specification: ../../../vim/host/VirtualNic/Specification.rst


vim.host.VirtualNic.Config
==========================
  The `HostVirtualNicConfig`_ data object describes the Virtual NIC configuration. It represents both the configured properties on a `HostVirtualNic`_ and identification information.
:extends: vmodl.DynamicData_

Attributes:
    changeOperation (`str`_, optional):

       Change operation to apply on this configuration specification.See `HostConfigChangeOperation`_ 
    device (`str`_, optional):

       Virtual NIC device to which configuration applies ( `HostVirtualNic`_ . `device`_ ).
    portgroup (`str`_):

       If the Virtual NIC is connecting to a vSwitch, this property is the name of portgroup connected. If the Virtual NIC is connecting to a `DistributedVirtualSwitch`_ , this property is ignored.
    spec (`vim.host.VirtualNic.Specification`_, optional):

       Specification of the virtual network adapter.
