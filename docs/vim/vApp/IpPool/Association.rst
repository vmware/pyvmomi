.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Network: ../../../vim/Network.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.vApp.IpPool.Association
===========================
  Information about a network or portgroup that is associated to an IP pool.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    network (`vim.Network`_, privilege: System.Read, optional):

       The network object
    networkName (`str`_):

       The name of the network or portgroupThis field is only used when querying existing IP pools. It is ignored when creating or updating pools.
