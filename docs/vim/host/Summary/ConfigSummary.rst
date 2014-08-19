
vim.host.Summary.ConfigSummary
==============================
  An overview of the key configuration parameters.
:extends: vmodl.DynamicData_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the host.
    port (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The port number.
    sslThumbprint (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The SSL thumbprint of the host, if known.
    product (`vim.AboutInfo <vim/AboutInfo.rst>`_, optional):

       Information about the software running on the host, if known.The current supported hosts are ESX Server 2.0.1 (and later) and VMware Server 2.0.0 (and later).
    vmotionEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not VMotion is enabled on this host.
    faultToleranceEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not Fault Tolerance logging is enabled on this host.
    featureVersion ([`vim.host.FeatureVersionInfo <vim/host/FeatureVersionInfo.rst>`_], optional):

       List of feature-specific version information. Each element refers to the version information for a specific feature.
    agentVmDatastore (`vim.Datastore <vim/Datastore.rst>`_, optional):

       Datastore used to deploy Agent VMs on for this host.
    agentVmNetwork (`vim.Network <vim/Network.rst>`_, optional):

       Management network for Agent VMs.
