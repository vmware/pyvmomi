.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.KeyValue: ../../../vim/KeyValue.rst

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.HostProxySwitch.HostLagConfig
======================================
  This data object type describes the set of Uplink Ports in Link Aggregation Control Protocol group.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    lagKey (`str`_):

    lagName (`str`_, optional):

    uplinkPort ([`vim.KeyValue`_], optional):

       The list of Uplink Ports in the Link Aggregation Control Protocol group. This property contains the keys and names of such ports.
