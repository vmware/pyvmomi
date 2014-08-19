
vim.host.InternetScsiHba
========================
  This data object type describes the iSCSI host bus adapter interface.
:extends: vim.host.HostBusAdapter_

Attributes:
    isSoftwareBased (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if this host bus adapter is a software based initiator utilizing the hosting system's existing TCP/IP network connection
    canBeDisabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Can this adapter be disabled
    networkBindingSupport (`vim.host.InternetScsiHba.NetworkBindingSupportType <vim/host/InternetScsiHba/NetworkBindingSupportType.rst>`_, optional):

       Specifies if this iSCSI Adapter requires a bound network interface to function.
    discoveryCapabilities (`vim.host.InternetScsiHba.DiscoveryCapabilities <vim/host/InternetScsiHba/DiscoveryCapabilities.rst>`_):

       The discovery capabilities for this host bus adapter.
    discoveryProperties (`vim.host.InternetScsiHba.DiscoveryProperties <vim/host/InternetScsiHba/DiscoveryProperties.rst>`_):

       The discovery settings for this host bus adapter.
    authenticationCapabilities (`vim.host.InternetScsiHba.AuthenticationCapabilities <vim/host/InternetScsiHba/AuthenticationCapabilities.rst>`_):

       The authentication capabilities for this host bus adapter.
    authenticationProperties (`vim.host.InternetScsiHba.AuthenticationProperties <vim/host/InternetScsiHba/AuthenticationProperties.rst>`_):

       The authentication settings for this host bus adapter. All static and discovery targets will inherit the use of these settings unless their authentication settings are explicitly set.
    digestCapabilities (`vim.host.InternetScsiHba.DigestCapabilities <vim/host/InternetScsiHba/DigestCapabilities.rst>`_, optional):

       The authentication capabilities for this host bus adapter.
    digestProperties (`vim.host.InternetScsiHba.DigestProperties <vim/host/InternetScsiHba/DigestProperties.rst>`_, optional):

       The digest settings for this host bus adapter. All static and discovery targets will inherit the use of these properties unless their digest settings are explicitly set.
    ipCapabilities (`vim.host.InternetScsiHba.IPCapabilities <vim/host/InternetScsiHba/IPCapabilities.rst>`_):

       The IP capabilities for this host bus adapter.
    ipProperties (`vim.host.InternetScsiHba.IPProperties <vim/host/InternetScsiHba/IPProperties.rst>`_):

       The IP settings for this host bus adapter.
    supportedAdvancedOptions ([`vim.option.OptionDef <vim/option/OptionDef.rst>`_], optional):

       A list of supported key/value pair advanced options for the host bus adapter including their type information.
    advancedOptions ([`vim.host.InternetScsiHba.ParamValue <vim/host/InternetScsiHba/ParamValue.rst>`_], optional):

       A list of the current options settings for the host bus adapter.
    iScsiName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The iSCSI name of this host bus adapter.
    iScsiAlias (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The iSCSI alias of this host bus adapter.
    configuredSendTarget ([`vim.host.InternetScsiHba.SendTarget <vim/host/InternetScsiHba/SendTarget.rst>`_], optional):

       The configured iSCSI send target entries.
    configuredStaticTarget ([`vim.host.InternetScsiHba.StaticTarget <vim/host/InternetScsiHba/StaticTarget.rst>`_], optional):

       The configured iSCSI static target entries.
    maxSpeedMb (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum supported link speed of the port in megabits per second.
    currentSpeedMb (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The Current operating link speed of the port in megabits per second.
