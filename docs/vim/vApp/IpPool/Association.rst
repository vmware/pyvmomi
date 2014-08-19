
vim.vApp.IpPool.Association
===========================
  Information about a network or portgroup that is associated to an IP pool.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    network (`vim.Network <vim/Network.rst>`_, privilege: System.Read, optional):

       The network object
    networkName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the network or portgroupThis field is only used when querying existing IP pools. It is ignored when creating or updating pools.
