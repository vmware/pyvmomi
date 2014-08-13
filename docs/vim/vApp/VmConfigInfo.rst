.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _installBootRequired: ../../vim/VirtualApp/Summary.rst#installBootRequired

.. _vim.vApp.ProductInfo: ../../vim/vApp/ProductInfo.rst

.. _vim.vApp.PropertyInfo: ../../vim/vApp/PropertyInfo.rst

.. _vim.vApp.OvfSectionInfo: ../../vim/vApp/OvfSectionInfo.rst

.. _vim.vApp.IPAssignmentInfo: ../../vim/vApp/IPAssignmentInfo.rst


vim.vApp.VmConfigInfo
=====================
  VM Configuration.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    product ([`vim.vApp.ProductInfo`_], optional):

       Information about the package content.
    property ([`vim.vApp.PropertyInfo`_], optional):

       List of properties
    ipAssignment (`vim.vApp.IPAssignmentInfo`_):

       IP assignment policy and DHCP support configuration.
    eula ([`str`_], optional):

       End User Liceses Agreements.
    ovfSection ([`vim.vApp.OvfSectionInfo`_], optional):

       List of uninterpreted OVF meta-data sections.
    ovfEnvironmentTransport ([`str`_], optional):

       List the transports to use for properties. Supported values are: iso and com.vmware.guestInfo.
    installBootRequired (`bool`_):

       Specifies whether the VM needs an initial boot before the deployment is complete.Not relevant for vApps. This means that the value is always false when reading the configuration and is ignored when setting the configuration.If a vApp requires an install boot (because one of its VMs does), this is visible on the `installBootRequired`_ field of the vApp.
    installBootStopDelay (`int`_):

       Specifies the delay in seconds to wait for the VM to power off after the initial boot (used only if installBootRequired is true). A value of 0 means wait forever.Not relevant for vApps. This means that the value is always false when reading the configuration and is ignored when setting the configuration.
