.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.Extension.OvfConsumerInfo
=============================
  This data object contains configuration for extensions that also extend the OVF functionality of vCenter server.Note:This feature is for internal use only.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    callbackUrl (`str`_):

       Callback url for the OVF consumer. This URL must point to a SOAP API implementing the OVF consumer interface.Example: https://extension-host:8081/This callback is for internal use only.
    sectionType ([`str`_]):

       A list of fully qualified OVF section types that this consumer handles.Fully qualified means that each section type must be prefixed with its namespace enclosed in curly braces. See the examples below.An InvalidArgument error is thrown if there is overlap between OVF consumers, meaning that the same section type appears in the sectionType list of more than one OVF consumer.Example: [ "{http://www.vmware.com/schema/vServiceManager}vServiceDependency", "{http://www.vmware.com/schema/vServiceManager}vServiceBinding" ]
