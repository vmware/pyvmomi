
vim.host.PortGroup.Specification
================================
  This data object type describes the PortGroup specification representing the properties on a PortGroup that can be configured.
:extends: vmodl.DynamicData_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the port group.
    vlanId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The VLAN ID for ports using this port group. Possible values:
        * A value of 0 specifies that you do not want the port group associated with a VLAN.
        * A value from 1 to 4094 specifies a VLAN ID for the port group.
        * A value of 4095 specifies that the port group should use trunk mode, which allows the guest operating system to manage its own VLAN tags.
    vswitchName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The identifier of the virtual switch on which this port group is located.
    policy (`vim.host.NetworkPolicy <vim/host/NetworkPolicy.rst>`_):

       Policies on the port group take precedence over the ones specified on the virtual switch.
