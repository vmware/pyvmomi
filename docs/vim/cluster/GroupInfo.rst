.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _ClusterGroupInfo: ../../vim/cluster/GroupInfo.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.cluster.GroupInfo
=====================
   `ClusterGroupInfo`_ is the base type for all virtual machine and host groups. All virtual machines and hosts that are part of a group must be part of the same cluster.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    name (`str`_):

       Unique name of the group.
    userCreated (`bool`_, optional):

       Flag to indicate whether the group is created by the user or the system.
