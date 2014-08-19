
vim.host.FibreChannelOverEthernetTargetTransport
================================================
  Fibre Channel Over Ethernet transport information about a SCSI target. FCoE transport information is that of: the regular FC World Wide Node and Port Names; the VNPort MAC address and FCF MAC address which constitute a VN_Port to VF_Port Virtual Link; and the VLAN on which an FCoE target resides. More FCoE information can be found in the working draft of the T11's Fibre Channel Backbone 5 standard (FC-BB-5). The draft can be found at http://www.t11.org.
:extends: vim.host.FibreChannelTargetTransport_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    vnportMac (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       VNPort MAC address. This MAC address should be of the form "xx:xx:xx:xx:xx:xx", where 'x' is a hexadecimal digit. Valid MAC addresses are unicast addresses.
    fcfMac (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       FCF MAC address. This MAC address should be of the form "xx:xx:xx:xx:xx:xx", where 'x' is a hexadecimal digit. Valid MAC addresses are unicast addresses.
    vlanId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       VLAN ID. Valid VLAN IDs fall within the range [0,4094].
