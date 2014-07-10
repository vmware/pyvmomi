.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.option.OptionDef: ../../../vim/option/OptionDef.rst

.. _vim.host.InternetScsiHba.ParamValue: ../../../vim/host/InternetScsiHba/ParamValue.rst

.. _vim.host.InternetScsiHba.DigestProperties: ../../../vim/host/InternetScsiHba/DigestProperties.rst

.. _vim.host.InternetScsiHba.AuthenticationProperties: ../../../vim/host/InternetScsiHba/AuthenticationProperties.rst


vim.host.InternetScsiHba.StaticTarget
=====================================
  The iSCSI static target.
:extends: vmodl.DynamicData_

Attributes:
    address (`str`_):

       The IP address or hostname of the storage device.
    port (`int`_, optional):

       The TCP port of the storage device. If not specified, the standard default of 3260 is used.
    iScsiName (`str`_):

       The iSCSI name of the storage device.
    discoveryMethod (`str`_, optional):

       Discovery method each static target is discovered by some method define in TargetDiscoveryMethod.
    authenticationProperties (`vim.host.InternetScsiHba.AuthenticationProperties`_, optional):

       The authentication settings for this target.
    digestProperties (`vim.host.InternetScsiHba.DigestProperties`_, optional):

       The digest settings for this target.
    supportedAdvancedOptions (`vim.option.OptionDef`_, optional):

       A list of supported key/value pair advanced options for the host bus adapter including their type information.
    advancedOptions (`vim.host.InternetScsiHba.ParamValue`_, optional):

       A list of the current options settings for the host bus adapter.
    parent (`str`_, optional):

       The parent entity from which settings can be inherited. It can either be unset, or set to the device name of the host bus adapter or the name of the SendTarget.
