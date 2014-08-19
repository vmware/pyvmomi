
vim.host.LinkDiscoveryProtocolConfig
====================================
  Dataobject representing the link discovery protocol configuration for a virtual or distributed virtual switch.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    protocol (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The discovery protocol type. For valid values see `LinkDiscoveryProtocolConfigProtocolType <vim/host/LinkDiscoveryProtocolConfig/ProtocolType.rst>`_ .
    operation (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether to advertise or listen. For valid values see `LinkDiscoveryProtocolConfigOperationType <vim/host/LinkDiscoveryProtocolConfig/OperationType.rst>`_ .
