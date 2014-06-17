.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vim.host.FibreChannelHba: ../../vim/host/FibreChannelHba.rst

.. _vim.host.FibreChannelOverEthernetHba.LinkInfo: ../../vim/host/FibreChannelOverEthernetHba/LinkInfo.rst


vim.host.FibreChannelOverEthernetHba
====================================
  This data object type describes the FCoE host bus adapter interface. Terminology is borrowed from T11's working draft of the Fibre Channel Backbone 5 standard (FC-BB-5). The draft can be found at http://www.t11.org.
:extends: vim.host.FibreChannelHba_
:since: `vSphere API 5.0`_

Attributes:
    underlyingNic (`str`_):

       The name associated with this FCoE HBA's underlying FcoeNic.
    linkInfo (`vim.host.FibreChannelOverEthernetHba.LinkInfo`_):

       Link information that can be used to uniquely identify this FCoE HBA.
    isSoftwareFcoe (`bool`_):

       True if this host bus adapter is a software based FCoE initiator.
    markedForRemoval (`bool`_):

       True if this host bus adapter has been marked for removal.
