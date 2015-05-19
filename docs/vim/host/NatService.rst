.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.NatService.Specification: ../../vim/host/NatService/Specification.rst


vim.host.NatService
===================
  A network address translation (NAT) service instance provides firewall and network address translation services for a virtual network.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    key (`str`_):

       The instance ID of the NAT service.
    spec (`vim.host.NatService.Specification`_):

       The configurable properties for the NatService object.
