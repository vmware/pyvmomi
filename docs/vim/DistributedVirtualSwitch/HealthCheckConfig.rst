
vim.DistributedVirtualSwitch.HealthCheckConfig
==============================================
  The `DVSHealthCheckConfig <vim/DistributedVirtualSwitch/HealthCheckConfig.rst>`_ data object defines vSphere Distributed Switch health check configuration.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    enable (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if enable health check.
    interval (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Interval of health check, in minutes.
