.. _vim.host.IpConfig: ../../../vim/host/IpConfig.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.PhysicalNic.LinkSpeedDuplex: ../../../vim/host/PhysicalNic/LinkSpeedDuplex.rst


vim.host.PhysicalNic.Specification
==================================
  This data object type describes the physical network adapter specification representing the properties on a physical network adapter that can be configured once the object exists.
:extends: vmodl.DynamicData_

Attributes:
    ip (`vim.host.IpConfig`_, optional):

       The IP configuration on the physical network adapter (applies only to a hosted network adapter). The data object will be NULL on an ESX Server system.
    linkSpeed (`vim.host.PhysicalNic.LinkSpeedDuplex`_, optional):

       The link speed and duplexity that this physical network adapter is currently configured to use. If this property is not set, the physical network adapter autonegotiates its proper settings.
