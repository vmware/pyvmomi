.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.IpRouteEntry
=====================
  IpRouteEntry. Routing entries are individual static routes which combined with the default route form all of the routing rules for a host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    network (`str`_):

       Network of the routing entry Of the format "10.20.120.0" or "2001:db8::1428:57"
    prefixLength (`int`_):

       Prefix length of the network (this is the 22 in 10.20.120.0/22)
    gateway (`str`_):

       Gateway for the routing entry
    deviceName (`str`_, optional):

       If available the property indicates the device associated with the routing entry. This property can only be read from the server. It will be ignored if set by the client.
