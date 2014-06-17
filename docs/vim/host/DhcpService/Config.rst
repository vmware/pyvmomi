.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostConfigChangeOperation: ../../../vim/host/ConfigChange/Operation.rst

.. _vim.host.DhcpService.Specification: ../../../vim/host/DhcpService/Specification.rst


vim.host.DhcpService.Config
===========================
  This data object type describes the configuration of a DHCP service instance representing both the configured properties on the instance and identification information.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    changeOperation (`str`_, optional):

       Indicates the change operation to apply on this configuration specification.See `HostConfigChangeOperation`_ 
    key (`str`_):

       The instance ID of the DHCP service.
    spec (`vim.host.DhcpService.Specification`_):

       Specification of the DHCP service.
