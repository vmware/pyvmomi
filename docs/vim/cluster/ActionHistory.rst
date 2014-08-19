
vim.cluster.ActionHistory
=========================
  Base class for all action history.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    action (`vim.cluster.Action <vim/cluster/Action.rst>`_):

       The action that was executed recently.
    time (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       The time when the action was executed.
