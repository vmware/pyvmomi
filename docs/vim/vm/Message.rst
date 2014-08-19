
vim.vm.Message
==============
  Message data which is intended to be displayed according to the locale of a client.A `VirtualMachineMessage <vim/vm/Message.rst>`_ contains both a formatted, localized version of the text and the data needed to perform localization in conjunction with localization catalogs.Clients of the VIM API may use `SessionManager <vim/SessionManager.rst>`_ . `SetLocale <vim/SessionManager.rst#setLocale>`_ to cause the server to emit localized `text <vim/vm/Message.rst#text>`_ , or may perform client-side localization based on message catalogs provided by the `LocalizationManager <vim/LocalizationManager.rst>`_ .Message variables are always integers, e.g. {1} and {2}, which are 1-based indexes into `argument <vim/vm/Message.rst#argument>`_ .
   * The corresponding argument may be a recursive lookup:
   * 
   * `argument <vim/vm/Message.rst#argument>`_
   * = ["button.cancel", "msg.revert"]
   * CATALOG(locmsg,
   * `id <vim/vm/Message.rst#id>`_
   * ) = "Select '{1}' to {2}"
   * CATALOG(locmsg, button.cancel) = "Cancel"
   * CATALOG(locmsg, msg.revert) = "revert"
   * ==
   * 
   * `text <vim/vm/Message.rst#text>`_
   * = "Select 'Cancel' to revert"
   * If the recursive lookup fails, the argument is a plain string.
   * 
   * `argument <vim/vm/Message.rst#argument>`_
   * = ["127.0.0.1"]
   * CATALOG(locmsg,
   * `id <vim/vm/Message.rst#id>`_
   * ) = "IP address is {1}"
   * ==
   * 
   * `text <vim/vm/Message.rst#text>`_
   * "IP address is 127.0.0.1"See `LocalizationManager <vim/LocalizationManager.rst>`_ 
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A unique identifier for this particular message. This field is a key for looking up format strings in the locmsg catalog.
    argument ([`object <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Substitution arguments for variables in the localized message. Substitution variables in the format string identified by `id <vim/vm/Message.rst#id>`_ are 1-based indexes into this array. Substitution variable {1} corresponds to argument[0], etc.
    text (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Text in session locale. Use `SessionManager <vim/SessionManager.rst>`_ . `SetLocale <vim/SessionManager.rst#setLocale>`_ to change the session locale.
