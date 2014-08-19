
vim.LocalizationManager
=======================
   `LocalizationManager <vim/LocalizationManager.rst>`_ provides access to descriptions of the message catalogs that are available for client-side message localization.Clients of the VIM API may use `SessionManager <vim/SessionManager.rst>`_ . `SetLocale <vim/SessionManager.rst#setLocale>`_ to cause the server to emit localized messages, or may perform client-side localization based on message catalogs provided by the `LocalizationManager <vim/LocalizationManager.rst>`_ .A message catalog is a file that contains a set of key-value pairs.
   * The key is an ASCII string that identifies the message.
   * The value is a UTF-8 string that contains the text of the message, sometimes containing substitution variables.The server will localize fields tagged with 'localizable' based on the value of the `UserSession <vim/UserSession.rst>`_ . `locale <vim/UserSession.rst#locale>`_ and `messageLocale <vim/UserSession.rst#messageLocale>`_ properties which are set via `SessionManager <vim/SessionManager.rst>`_ . `SetLocale <vim/SessionManager.rst#setLocale>`_ .The following list shows some of the ways that vSphere uses localized messages.
   * Current task status (
   * `TaskInfo <vim/TaskInfo.rst>`_
   * .
   * `description <vim/TaskInfo.rst#description>`_
   * )
   * Events (
   * `VirtualMachineMessage <vim/vm/Message.rst>`_
   * .
   * `text <vim/vm/Message.rst#text>`_
   * and Questions (
   * `VirtualMachineQuestionInfo <vim/vm/QuestionInfo.rst>`_
   * .
   * `text <vim/vm/QuestionInfo.rst#text>`_
   * )
   * Faults (
   * `MethodFault <vmodl/MethodFault.rst>`_
   * .
   * `faultMessage <vmodl/MethodFault.rst#faultMessage>`_
   * )
   * `HostProfile <vim/profile/host/HostProfile.rst>`_
   * and
   * `ClusterProfile <vim/profile/cluster/ClusterProfile.rst>`_
   * descriptions (
   * `Profile <vim/profile/Profile.rst>`_
   * .
   * `ProfileDescription <vim/profile/Profile/Description.rst>`_
   * .
   * `description <vim/profile/Profile.rst#description>`_
   * returned by the
   * `Profile <vim/profile/Profile.rst>`_
   * .
   * `RetrieveDescription <vim/profile/Profile.rst#retrieveDescription>`_
   * method)


:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


Attributes
----------
    catalog ([`vim.LocalizationManager.MessageCatalog <vim/LocalizationManager/MessageCatalog.rst>`_]):
      privilege: System.View
       Fetches the descriptions of all the client-side localization message catalogs available for the current session locale.


Methods
-------


