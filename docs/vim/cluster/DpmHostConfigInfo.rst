.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ClusterDpmConfigInfo: ../../vim/cluster/DpmConfigInfo.rst

.. _vim.cluster.DpmConfigInfo.DpmBehavior: ../../vim/cluster/DpmConfigInfo/DpmBehavior.rst


vim.cluster.DpmHostConfigInfo
=============================
  DPM configuration for a single host. This makes it possible to override the default behavior for an individual host.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    key (`vim.HostSystem`_):

       Reference to the host.
    enabled (`bool`_, optional):

       Flag to indicate whether or not VirtualCenter is allowed to perform any power related operations or recommendations for this host. If this flag is false, the host is effectively excluded from DPM service.If no individual DPM specification exists for a host, this property defaults to true.
    behavior (`vim.cluster.DpmConfigInfo.DpmBehavior`_, optional):

       Specifies the particular DPM behavior for this host.See `ClusterDpmConfigInfo`_ 
