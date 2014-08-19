
vim.host.InternetScsiHba.StaticTarget
=====================================
  The iSCSI static target.
:extends: vmodl.DynamicData_

Attributes:
    address (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The IP address or hostname of the storage device.
    port (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The TCP port of the storage device. If not specified, the standard default of 3260 is used.
    iScsiName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The iSCSI name of the storage device.
    discoveryMethod (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Discovery method each static target is discovered by some method define in TargetDiscoveryMethod.
    authenticationProperties (`vim.host.InternetScsiHba.AuthenticationProperties <vim/host/InternetScsiHba/AuthenticationProperties.rst>`_, optional):

       The authentication settings for this target.
    digestProperties (`vim.host.InternetScsiHba.DigestProperties <vim/host/InternetScsiHba/DigestProperties.rst>`_, optional):

       The digest settings for this target.
    supportedAdvancedOptions ([`vim.option.OptionDef <vim/option/OptionDef.rst>`_], optional):

       A list of supported key/value pair advanced options for the host bus adapter including their type information.
    advancedOptions ([`vim.host.InternetScsiHba.ParamValue <vim/host/InternetScsiHba/ParamValue.rst>`_], optional):

       A list of the current options settings for the host bus adapter.
    parent (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The parent entity from which settings can be inherited. It can either be unset, or set to the device name of the host bus adapter or the name of the SendTarget.
