
vim.cluster.GroupInfo
=====================
   `ClusterGroupInfo <vim/cluster/GroupInfo.rst>`_ is the base type for all virtual machine and host groups. All virtual machines and hosts that are part of a group must be part of the same cluster.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Unique name of the group.
    userCreated (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether the group is created by the user or the system.
