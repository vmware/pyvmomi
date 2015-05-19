.. _str: https://docs.python.org/2/library/stdtypes.html

.. _text: ../../vim/vm/Message.rst#text

.. _object: https://docs.python.org/2/library/stdtypes.html

.. _argument: ../../vim/vm/Message.rst#argument

.. _SetLocale: ../../vim/SessionManager.rst#setLocale

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _SessionManager: ../../vim/SessionManager.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _LocalizationManager: ../../vim/LocalizationManager.rst

.. _VirtualMachineMessage: ../../vim/vm/Message.rst


vim.vm.Message
==============
  Message data which is intended to be displayed according to the locale of a client.A `VirtualMachineMessage`_ contains both a formatted, localized version of the text and the data needed to perform localization in conjunction with localization catalogs.Clients of the VIM API may use `SessionManager`_ . `SetLocale`_ to cause the server to emit localized `text`_ , or may perform client-side localization based on message catalogs provided by the `LocalizationManager`_ .Message variables are always integers, e.g. {1} and {2}, which are 1-based indexes into `argument`_ .
   * The corresponding argument may be a recursive lookup:
   * 
   * `argument`_
   * = ["button.cancel", "msg.revert"]
   * CATALOG(locmsg,
   * `id`_
   * ) = "Select '{1}' to {2}"
   * CATALOG(locmsg, button.cancel) = "Cancel"
   * CATALOG(locmsg, msg.revert) = "revert"
   * ==
   * 
   * `text`_
   * = "Select 'Cancel' to revert"
   * If the recursive lookup fails, the argument is a plain string.
   * 
   * `argument`_
   * = ["127.0.0.1"]
   * CATALOG(locmsg,
   * `id`_
   * ) = "IP address is {1}"
   * ==
   * 
   * `text`_
   * "IP address is 127.0.0.1"See `LocalizationManager`_ 
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    id (`str`_):

       A unique identifier for this particular message. This field is a key for looking up format strings in the locmsg catalog.
    argument ([`object`_], optional):

       Substitution arguments for variables in the localized message. Substitution variables in the format string identified by `id`_ are 1-based indexes into this array. Substitution variable {1} corresponds to argument[0], etc.
    text (`str`_, optional):

       Text in session locale. Use `SessionManager`_ . `SetLocale`_ to change the session locale.
