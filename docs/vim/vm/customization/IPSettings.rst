
vim.vm.customization.IPSettings
===============================
  IP settings for a virtual network adapter.
:extends: vmodl.DynamicData_

Attributes:
    ip (`vim.vm.customization.IpGenerator <vim/vm/customization/IpGenerator.rst>`_):

       Specification to obtain a unique IP address for this virtual network adapter.
    subnetMask (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Subnet mask for this virtual network adapter.
    gateway ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       For a virtual network adapter with a static IP address, this data object type contains a list of gateways, in order of preference.
    ipV6Spec (`vim.vm.customization.IPSettings.IpV6AddressSpec <vim/vm/customization/IPSettings/IpV6AddressSpec.rst>`_, optional):

       This contains the IpGenerator, subnet mask and gateway info for all the ipv6 addresses associated with the virtual network adapter.
    dnsServerList ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       A list of server IP addresses to use for DNS lookup in a Windows guest operating system. In Windows, these settings are adapter-specific, whereas in Linux, they are global. As a result, the Linux guest customization process ignores this setting and looks for its DNS servers in the globalIPSettings object.Specify these servers in order of preference. If this list is not empty, and if a DHCP IpGenerator is used, then these settings override the DHCP settings.
    dnsDomain (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       A DNS domain suffix such as vmware.com.
    primaryWINS (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The IP address of the primary WINS server. This property is ignored for Linux guest operating systems.
    secondaryWINS (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The IP address of the secondary WINS server. This property is ignored for Linux guest operating systems.
    netBIOS (`vim.vm.customization.IPSettings.NetBIOSMode <vim/vm/customization/IPSettings/NetBIOSMode.rst>`_, optional):

       NetBIOS setting for Windows.
