.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _LinkDiscoveryProtocolConfigProtocolType: ../../vim/host/LinkDiscoveryProtocolConfig/ProtocolType.rst

.. _LinkDiscoveryProtocolConfigOperationType: ../../vim/host/LinkDiscoveryProtocolConfig/OperationType.rst


vim.host.LinkDiscoveryProtocolConfig
====================================
  Dataobject representing the link discovery protocol configuration for a virtual or distributed virtual switch.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    protocol (`str`_):

       The discovery protocol type. For valid values see `LinkDiscoveryProtocolConfigProtocolType`_ .
    operation (`str`_):

       Whether to advertise or listen. For valid values see `LinkDiscoveryProtocolConfigOperationType`_ .
