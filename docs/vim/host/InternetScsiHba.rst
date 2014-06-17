.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.option.OptionDef: ../../vim/option/OptionDef.rst

.. _vim.host.HostBusAdapter: ../../vim/host/HostBusAdapter.rst

.. _vim.host.InternetScsiHba.ParamValue: ../../vim/host/InternetScsiHba/ParamValue.rst

.. _vim.host.InternetScsiHba.SendTarget: ../../vim/host/InternetScsiHba/SendTarget.rst

.. _vim.host.InternetScsiHba.IPProperties: ../../vim/host/InternetScsiHba/IPProperties.rst

.. _vim.host.InternetScsiHba.StaticTarget: ../../vim/host/InternetScsiHba/StaticTarget.rst

.. _vim.host.InternetScsiHba.IPCapabilities: ../../vim/host/InternetScsiHba/IPCapabilities.rst

.. _vim.host.InternetScsiHba.DigestProperties: ../../vim/host/InternetScsiHba/DigestProperties.rst

.. _vim.host.InternetScsiHba.DigestCapabilities: ../../vim/host/InternetScsiHba/DigestCapabilities.rst

.. _vim.host.InternetScsiHba.DiscoveryProperties: ../../vim/host/InternetScsiHba/DiscoveryProperties.rst

.. _vim.host.InternetScsiHba.DiscoveryCapabilities: ../../vim/host/InternetScsiHba/DiscoveryCapabilities.rst

.. _vim.host.InternetScsiHba.AuthenticationProperties: ../../vim/host/InternetScsiHba/AuthenticationProperties.rst

.. _vim.host.InternetScsiHba.NetworkBindingSupportType: ../../vim/host/InternetScsiHba/NetworkBindingSupportType.rst

.. _vim.host.InternetScsiHba.AuthenticationCapabilities: ../../vim/host/InternetScsiHba/AuthenticationCapabilities.rst


vim.host.InternetScsiHba
========================
  This data object type describes the iSCSI host bus adapter interface.
:extends: vim.host.HostBusAdapter_

Attributes:
    isSoftwareBased (`bool`_):

       True if this host bus adapter is a software based initiator utilizing the hosting system's existing TCP/IP network connection
    canBeDisabled (`bool`_, optional):

       Can this adapter be disabled
    networkBindingSupport (`vim.host.InternetScsiHba.NetworkBindingSupportType`_, optional):

       Specifies if this iSCSI Adapter requires a bound network interface to function.
    discoveryCapabilities (`vim.host.InternetScsiHba.DiscoveryCapabilities`_):

       The discovery capabilities for this host bus adapter.
    discoveryProperties (`vim.host.InternetScsiHba.DiscoveryProperties`_):

       The discovery settings for this host bus adapter.
    authenticationCapabilities (`vim.host.InternetScsiHba.AuthenticationCapabilities`_):

       The authentication capabilities for this host bus adapter.
    authenticationProperties (`vim.host.InternetScsiHba.AuthenticationProperties`_):

       The authentication settings for this host bus adapter. All static and discovery targets will inherit the use of these settings unless their authentication settings are explicitly set.
    digestCapabilities (`vim.host.InternetScsiHba.DigestCapabilities`_, optional):

       The authentication capabilities for this host bus adapter.
    digestProperties (`vim.host.InternetScsiHba.DigestProperties`_, optional):

       The digest settings for this host bus adapter. All static and discovery targets will inherit the use of these properties unless their digest settings are explicitly set.
    ipCapabilities (`vim.host.InternetScsiHba.IPCapabilities`_):

       The IP capabilities for this host bus adapter.
    ipProperties (`vim.host.InternetScsiHba.IPProperties`_):

       The IP settings for this host bus adapter.
    supportedAdvancedOptions (`vim.option.OptionDef`_, optional):

       A list of supported key/value pair advanced options for the host bus adapter including their type information.
    advancedOptions (`vim.host.InternetScsiHba.ParamValue`_, optional):

       A list of the current options settings for the host bus adapter.
    iScsiName (`str`_):

       The iSCSI name of this host bus adapter.
    iScsiAlias (`str`_, optional):

       The iSCSI alias of this host bus adapter.
    configuredSendTarget (`vim.host.InternetScsiHba.SendTarget`_, optional):

       The configured iSCSI send target entries.
    configuredStaticTarget (`vim.host.InternetScsiHba.StaticTarget`_, optional):

       The configured iSCSI static target entries.
    maxSpeedMb (`int`_, optional):

       The maximum supported link speed of the port in megabits per second.
    currentSpeedMb (`int`_, optional):

       The Current operating link speed of the port in megabits per second.
