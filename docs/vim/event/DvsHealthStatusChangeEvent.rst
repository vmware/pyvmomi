.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst

.. _vim.dvs.HostMember.HealthCheckResult: ../../vim/dvs/HostMember/HealthCheckResult.rst


vim.event.DvsHealthStatusChangeEvent
====================================
  Health check status of an switch is changed.
:extends: vim.event.HostEvent_
:since: `vSphere API 5.1`_

Attributes:
    switchUuid (`str`_):

       UUID of the DVS the host is connected to.
    healthResult (`vim.dvs.HostMember.HealthCheckResult`_, optional):

       Health check status.
