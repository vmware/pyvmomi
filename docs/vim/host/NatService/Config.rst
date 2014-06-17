.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostConfigChangeOperation: ../../../vim/host/ConfigChange/Operation.rst

.. _vim.host.NatService.Specification: ../../../vim/host/NatService/Specification.rst


vim.host.NatService.Config
==========================
  This data object type describes the network address translation (NAT) service configuration representing both the configured properties on a NAT Service and identification information.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    changeOperation (`str`_, optional):

       Indicates the change operation to apply on this configuration specification.See `HostConfigChangeOperation`_ 
    key (`str`_):

       The instance ID of the NAT service.
    spec (`vim.host.NatService.Specification`_):

       The specification of the NAT service.
