.. _str: https://docs.python.org/2/library/stdtypes.html

.. _NetworkPolicy: ../../vim/host/NetworkPolicy.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.VirtualSwitch: ../../vim/host/VirtualSwitch.rst

.. _vim.host.NetworkPolicy: ../../vim/host/NetworkPolicy.rst

.. _vim.host.PortGroup.Port: ../../vim/host/PortGroup/Port.rst

.. _vim.host.PortGroup.Specification: ../../vim/host/PortGroup/Specification.rst


vim.host.PortGroup
==================
  This data object type is used to describe port groups. Port groups are used to group virtual network adapters on a virtual switch, associating them with networks and network policies.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_, optional):

       The linkable identifier.
    port (`vim.host.PortGroup.Port`_, optional):

       The ports that currently exist and are used on this port group.
    vswitch (`vim.host.VirtualSwitch`_, optional):

       The virtual switch that contains this port group.
    computedPolicy (`vim.host.NetworkPolicy`_):

       Computed network policies that are applicable for a port group. The inheritance scheme for PortGroup requires knowledge about the NetworkPolicy for a port group and its parent virtual switch as well as the logic for computing the results. This information is provided as a convenience so that callers need not duplicate the inheritance logic to determine the proper values for a network policy.See the description of the `NetworkPolicy`_ data object type for more information.
    spec (`vim.host.PortGroup.Specification`_):

       The specification of a port group.
