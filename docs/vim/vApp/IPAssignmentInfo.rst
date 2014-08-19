
vim.vApp.IPAssignmentInfo
=========================
  The IPAssignmentInfo class specifies how the guest software gets configured with IP addresses, including protocol type (IPv4 or IPv6) and the life-time of those IP addresses.A vApp/virtual machine can either use DHCP to acquire an IP configuration, or it can acquire its IP configuration through the use of the vSphere platform using the OVF environment's properties. The latter is a known as OVF-environment-assigned IP configuration.Guest software can be constructed to support DHCP , OVF assigned IP configuration, or both. The supportedAssignmentScheme property lists the supported schemes. This is typically specified by the author of a vApp.The deployer / operator of a vApp, specifies what IP allocation policy should be used:
   * Using DHCP, if the vApp and deployed network supports it
   * Transient Assignment, if the vApp supports OVF-assigned IP configuration and the network has an IP range configured.
   * Fixed Assignment, if the vApp supports OVF-assigned IP configuration.
   * Fixed Allocated, if the vApp supports OVF-assigned IP configuration and the network has an IP range configured.
   * 
   * Transient and fixed assignment differs in the life time of the IP allocation. For transient, IP addresses are automatically assigned on power-on and released on power-off. For fixed, the IP addresses are explicitly specified by the deployer and does not change between a power-on/power-off. Fixed allocated is a hybrid of transient and fixed assignment. IP addresses are allocated at first power-on and remain allocated on power-off.
   * The IPAssignment settings are global to a deployment. Thus, if a vApp or virtual machine is part of another vApp, then the settings are ignored, and the ones for the top-most vApp container is used.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    supportedAllocationScheme ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Specifies the IP allocation schemes supported by the guest software.When updating this field, an empty array will be interpreted as no changes. An array of the form [""] will clear all settings. Otherwise, the supplied value will overwrite the current setting.Reconfigure privilege: VApp.ApplicationConfig
    ipAllocationPolicy (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specifies how IP allocation should be managed by the VI platform. This is typically specified by the deployer. The set of valid options for the policy is based on the capabilities of the vApp software, as specified by the supportedAllocationSchemes property.Reconfigure privilege: VApp.InstanceConfig
    supportedIpProtocol ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Specifies the IP protocols supported by the guest software.When updating this field, an empty array will be interpreted as no changes. An array of the form [""] will clear all settings. Otherwise, the supplied value will overwrite the current setting.Reconfigure privilege: VApp.ApplicationConfig
    ipProtocol (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specifies the chosen IP protocol for this deployment. This must be one of the values in the supportedIpProtocol field.Reconfigure privilege: VApp.InstanceConfig
