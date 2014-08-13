.. _vim.Task: ../vim/Task.rst

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vim.LocalizationManager.MessageCatalog: ../vim/LocalizationManager/MessageCatalog.rst


vim.LocalizationManager
=======================
   `LocalizationManager`_ provides access to descriptions of the message catalogs that are available for client-side message localization.Clients of the VIM API may use `SessionManager`_ . `SetLocale`_ to cause the server to emit localized messages, or may perform client-side localization based on message catalogs provided by the `LocalizationManager`_ .A message catalog is a file that contains a set of key-value pairs.
   * The key is an ASCII string that identifies the message.
   * The value is a UTF-8 string that contains the text of the message, sometimes containing substitution variables.The server will localize fields tagged with 'localizable' based on the value of the `UserSession`_ . `locale`_ and `messageLocale`_ properties which are set via `SessionManager`_ . `SetLocale`_ .The following list shows some of the ways that vSphere uses localized messages.
   * Current task status (
   * `TaskInfo`_
   * .
   * `description`_
   * )
   * Events (
   * `VirtualMachineMessage`_
   * .
   * `text`_
   * and Questions (
   * `VirtualMachineQuestionInfo`_
   * .
   * `text`_
   * )
   * Faults (
   * `MethodFault`_
   * .
   * `faultMessage`_
   * )
   * `HostProfile`_
   * and
   * `ClusterProfile`_
   * descriptions (
   * `Profile`_
   * .
   * `ProfileDescription`_
   * .
   * `description`_
   * returned by the
   * `Profile`_
   * .
   * `RetrieveDescription`_
   * method)


:since: `vSphere API 4.0`_


Attributes
----------
    catalog ([`vim.LocalizationManager.MessageCatalog`_]):
      privilege: System.View
       Fetches the descriptions of all the client-side localization message catalogs available for the current session locale.


Methods
-------


