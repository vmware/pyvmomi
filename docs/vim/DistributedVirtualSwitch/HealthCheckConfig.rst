.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _DVSHealthCheckConfig: ../../vim/DistributedVirtualSwitch/HealthCheckConfig.rst


vim.DistributedVirtualSwitch.HealthCheckConfig
==============================================
  The `DVSHealthCheckConfig`_ data object defines vSphere Distributed Switch health check configuration.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    enable (`bool`_, optional):

       True if enable health check.
    interval (`int`_, optional):

       Interval of health check, in minutes.
