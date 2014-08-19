
vmodl.LocalizableMessage
========================
  Message data which is intended to be displayed according to the locale of a client.A `LocalizableMessage <vmodl/LocalizableMessage.rst>`_ contains both a formatted, localized version of the text and the data needed to perform localization in conjunction with localization catalogs.Clients of the VIM API may use vim.SessionManager.setLocale() to cause the server to emit a localized `message <vmodl/LocalizableMessage.rst#message>`_ , or may perform client-side localization based on message catalogs provided by the server.
   * If the substition variable is a string, no further lookup is required.
   * 
   * `arg <vmodl/LocalizableMessage.rst#arg>`_
   * = [("address" = "127.0.0.1")]
   * CATALOG(locmsg,
   * `key <vmodl/LocalizableMessage.rst#key>`_
   * ) = "IP address is {address}"
   * ==
   * 
   * `message <vmodl/LocalizableMessage.rst#message>`_
   * = "IP address is 127.0.0.1"
   * If the substitution variable is an integer, value is a lookup key.
   * 
   * `arg <vmodl/LocalizableMessage.rst#arg>`_
   * = [("1" = "button.cancel"), ("2" = "msg.revert")]
   * CATALOG(locmsg,
   * `key <vmodl/LocalizableMessage.rst#key>`_
   * ) = "Select '{1}' to {2}"
   * CATALOG(locmsg, button.cancel) = "Cancel"
   * CATALOG(locmsg, msg.revert) = "revert"
   * ==
   * 
   * `message <vmodl/LocalizableMessage.rst#message>`_
   * = "Select 'Cancel' to revert"
   * If the variable contains '@', value is a label lookup in another catalog, where {name.@CATALOG.prefix} looks up prefix.
   * `arg <vmodl/LocalizableMessage.rst#arg>`_
   * [name].label in CATALOG.
   * 
   * `arg <vmodl/LocalizableMessage.rst#arg>`_
   * = [("field" = "queued")]
   * CATALOG(locmsg,
   * `key <vmodl/LocalizableMessage.rst#key>`_
   * ) = "State is {field.@enum.TaskInfo.State}"
   * CATALOG(enum, TaskInfo.State.queued.label) is "Queued"
   * ==
   * 
   * `message <vmodl/LocalizableMessage.rst#message>`_
   * = "State is Queued"
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vmodlversionversion1>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Unique key identifying the message in the localized message catalog.
    arg ([`vmodl.KeyAnyValue <vmodl/KeyAnyValue.rst>`_], optional):

       Substitution arguments for variables in the localized message.
    message (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Message in session locale. Use vim.SessionManager.setLocale() to change the session locale.
