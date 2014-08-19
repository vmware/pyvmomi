
vim.host.FibreChannelOverEthernetHba.LinkInfo
=============================================
  Represents FCoE link information. The link information represents a VNPort to VFPort Virtual Link, as described in the FC-BB-5 standard, with the addition of the VLAN ID over which a link exists.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    vnportMac (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       VNPort MAC address, as defined by the FC-BB-5 standard. This MAC address should be of the form "xx:xx:xx:xx:xx:xx", where 'x' is a hexadecimal digit. Valid MAC addresses are unicast addresses.
    fcfMac (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       FCF MAC address, also known as the VFPort MAC address in the FC-BB-5 standard. This MAC address should be of the form "xx:xx:xx:xx:xx:xx", where 'x' is a hexadecimal digit. Valid MAC addresses are unicast addresses.
    vlanId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       VLAN ID. This field represents the VLAN on which an FCoE HBA was discovered. Valid numbers fall into the range [0,4094].
