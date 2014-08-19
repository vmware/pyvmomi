
vim.host.VirtualNic.Config
==========================
  The `HostVirtualNicConfig <vim/host/VirtualNic/Config.rst>`_ data object describes the Virtual NIC configuration. It represents both the configured properties on a `HostVirtualNic <vim/host/VirtualNic.rst>`_ and identification information.
:extends: vmodl.DynamicData_

Attributes:
    changeOperation (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Change operation to apply on this configuration specification.See `HostConfigChangeOperation <vim/host/ConfigChange/Operation.rst>`_ 
    device (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Virtual NIC device to which configuration applies ( `HostVirtualNic <vim/host/VirtualNic.rst>`_ . `device <vim/host/VirtualNic.rst#device>`_ ).
    portgroup (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       If the Virtual NIC is connecting to a vSwitch, this property is the name of portgroup connected. If the Virtual NIC is connecting to a `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ , this property is ignored.
    spec (`vim.host.VirtualNic.Specification <vim/host/VirtualNic/Specification.rst>`_, optional):

       Specification of the virtual network adapter.
