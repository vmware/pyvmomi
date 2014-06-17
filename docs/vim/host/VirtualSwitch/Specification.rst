.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.NetworkPolicy: ../../../vim/host/NetworkPolicy.rst

.. _vim.host.VirtualSwitch.Bridge: ../../../vim/host/VirtualSwitch/Bridge.rst


vim.host.VirtualSwitch.Specification
====================================
  This data object type describes the VirtualSwitch specification representing the properties on a VirtualSwitch that can be configured once the object exists.
:extends: vmodl.DynamicData_

Attributes:
    numPorts (`int`_):

       The number of ports that this virtual switch is configured to use. Changing this setting does not take effect until the next reboot. The maximum value is 1024, although other constraints, such as memory limits, may establish a lower effective limit.
    bridge (`vim.host.VirtualSwitch.Bridge`_, optional):

       The bridge specification describes how physical network adapters can be bridged to a virtual switch.
    policy (`vim.host.NetworkPolicy`_, optional):

       The virtual switch policy specification. This has a lower precedence than PortGroup. If the policy property is not set and you are creating a virtual switch, then a default policy property setting is used. If the policy property is not set and you are updating a virtual switch, then the policy will be unchanged.
    mtu (`int`_, optional):

       The maximum transmission unit (MTU) of the virtual switch in bytes.
