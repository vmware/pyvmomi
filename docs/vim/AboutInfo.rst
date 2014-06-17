.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst


vim.AboutInfo
=============
  This data object type describes system information including the name, type, version, and build number.
:extends: vmodl.DynamicData_

Attributes:
    name (`str`_):

       Short form of the product name.
    fullName (`str`_):

       The complete product name, including the version information.
    vendor (`str`_):

       Name of the vendor of this product.
    version (`str`_):

       Dot-separated version string. For example, "1.2".
    build (`str`_):

       Build string for the server on which this call is made. For example, x.y.z-num. This string does not apply to the API.
    localeVersion (`str`_, optional):

       Version of the message catalog for the current session's locale.
    localeBuild (`str`_, optional):

       Build number for the current session's locale. Typically, this is a small number reflecting a localization change from the normal product build.
    osType (`str`_):

       Operating system type and architecture.Examples of values are:
        * "win32-x86" - For x86-based Windows systems.
        * "linux-x86" - For x86-based Linux systems.
        * "vmnix-x86" - For the x86 ESX Server microkernel.
        * 
    productLineId (`str`_):

       The product ID is a unique identifier for a product line.Examples of values are:
        * "gsx" - For the VMware Server product.
        * "esx" - For the ESX product.
        * "embeddedEsx" - For the ESXi product.
        * "vpx" - For the VirtualCenter product.
        * 
    apiType (`str`_):

       Indicates whether or not the service instance represents a standalone host. If the service instance represents a standalone host, then the physical inventory for that service instance is fixed to that single host. VirtualCenter server provides additional features over single hosts. For example, VirtualCenter offers multi-host management.Examples of values are:
        * "VirtualCenter" - For a VirtualCenter instance.
        * "HostAgent" - For host agent on an ESX Server or VMware Server host.
        * 
    apiVersion (`str`_):

       The version of the API as a dot-separated string. For example, "1.0.0".
    instanceUuid (`str`_, optional):

       A globally unique identifier associated with this service instance.
    licenseProductName (`str`_, optional):

       The license product name
    licenseProductVersion (`str`_, optional):

       The license product version
