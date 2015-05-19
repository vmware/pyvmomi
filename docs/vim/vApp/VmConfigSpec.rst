.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _VAppPropertyInfo: ../../vim/vApp/PropertyInfo.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _VAppIPAssignmentInfo: ../../vim/vApp/IPAssignmentInfo.rst

.. _vim.vApp.ProductSpec: ../../vim/vApp/ProductSpec.rst

.. _vim.vApp.PropertySpec: ../../vim/vApp/PropertySpec.rst

.. _vim.vApp.OvfSectionSpec: ../../vim/vApp/OvfSectionSpec.rst

.. _vim.vApp.IPAssignmentInfo: ../../vim/vApp/IPAssignmentInfo.rst


vim.vApp.VmConfigSpec
=====================
  vApp related configuration of a VM.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    product ([`vim.vApp.ProductSpec`_], optional):

       Information about the product.Reconfigure privilege: VApp.ApplicationConfig
    property ([`vim.vApp.PropertySpec`_], optional):

       List of properties.Adding and editing properties requires various privileges depending on which fields are affected. See `VAppPropertyInfo`_ for details.Deleting properties requires the privilege VApp.ApplicationConfig.
    ipAssignment (`vim.vApp.IPAssignmentInfo`_, optional):

       IP assignment policy and DHCP support configuration.Reconfigure privilege: See `VAppIPAssignmentInfo`_ 
    eula ([`str`_], optional):

       End User Liceses Agreements.If this list is set, it replaces all exiting licenses. An empty list will not make any changes to installed licenses. A list with a single element {""} will remove all licenses and leave an empty list.Reconfigure privilege: VApp.ApplicationConfig
    ovfSection ([`vim.vApp.OvfSectionSpec`_], optional):

       List of uninterpreted OVF meta-data sections.Reconfigure privilege: VApp.ApplicationConfig
    ovfEnvironmentTransport ([`str`_], optional):

       List the transports to use for properties. Supported values are: iso and com.vmware.guestInfo.If this list is set, it replaces all exiting entries. An empty list will not make any changes. A list with a single element {""} will clear the list of transports.Reconfigure privilege: VApp.ApplicationConfig
    installBootRequired (`bool`_, optional):

       If this is on a VirtualMachine object, it specifies whether the VM needs an initial boot before the deployment is complete. If this is on a vApp object, it indicates than one or more VMs needs an initial reboot. This flag is automatically reset once the reboot has happened.Reconfigure privilege: VApp.ApplicationConfig
    installBootStopDelay (`int`_, optional):

       Specifies the delay in seconds to wait for the VM to power off after the initial boot (used only if installBootRequired is true). A value of 0 means wait forever.Reconfigure privilege: VApp.ApplicationConfig
