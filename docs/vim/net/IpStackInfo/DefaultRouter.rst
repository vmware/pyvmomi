.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _NetIpStackInfoPreference: ../../../vim/net/IpStackInfo/Preference.rst


vim.net.IpStackInfo.DefaultRouter
=================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    ipAddress (`str`_):

       Unicast IP address of a next-hop router.
    device (`str`_):

       This value will contain the name of the interface as reported by the operationg system.
    lifetime (`datetime`_):

       When this entry will no longer valid. For IPv6 this value see For IPv6 RFC 2462 sections 4.2 and 6.3.4.
    preference (`str`_):

       Value of this entry compared to others that this IP stack uses when making selection to route traffic on the default route when there are multiple default routers. Value must be one of `NetIpStackInfoPreference`_ 
