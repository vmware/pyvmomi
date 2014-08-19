
vim.cluster.DpmHostConfigInfo
=============================
  DPM configuration for a single host. This makes it possible to override the default behavior for an individual host.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    key (`vim.HostSystem <vim/HostSystem.rst>`_):

       Reference to the host.
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether or not VirtualCenter is allowed to perform any power related operations or recommendations for this host. If this flag is false, the host is effectively excluded from DPM service.If no individual DPM specification exists for a host, this property defaults to true.
    behavior (`vim.cluster.DpmConfigInfo.DpmBehavior <vim/cluster/DpmConfigInfo/DpmBehavior.rst>`_, optional):

       Specifies the particular DPM behavior for this host.See `ClusterDpmConfigInfo <vim/cluster/DpmConfigInfo.rst>`_ 
