
vim.action.SendEmailAction
==========================
  This data object type defines an email that is triggered by an alarm. You can use any elements of the `ActionParameter <vim/action/Action/ActionParameter.rst>`_ enumerated list as part of your strings to provide information available at runtime.
:extends: vim.action.Action_

Attributes:
    toList (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A comma-separated list of addresses to which the email notification is sent.
    ccList (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A comma-separated list of addresses that are cc'ed on the email notification.
    subject (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Subject of the email notification.
    body (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Content of the email notification.
