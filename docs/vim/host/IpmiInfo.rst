.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.IpmiInfo
=================
  The IpmiInfo data object contains IPMI (Intelligent Platform Management Interface) and BMC (Baseboard Management Controller) information for the host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    bmcIpAddress (`str`_, optional):

       IP address of the BMC on the host. It should be null terminated.
    bmcMacAddress (`str`_, optional):

       MAC address of the BMC on the host. The MAC address should be of the form xx:xx:xx:xx:xx:xx where each x is a hex digit. It should be null terminated.
    login (`str`_, optional):

       User ID for logging into the BMC. BMC usernames may be up to 16 characters and must be null terminated. Hence, a login comprises 17 or fewer characters.
    password (`str`_, optional):

       Password for logging into the BMC. Only used for configuration, returned as unset while reading. The password can be up to 16 characters and must be null terminated. Hence, a password comprises 17 or fewer characters.
