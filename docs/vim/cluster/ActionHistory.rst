.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.cluster.Action: ../../vim/cluster/Action.rst


vim.cluster.ActionHistory
=========================
  Base class for all action history.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    action (`vim.cluster.Action`_):

       The action that was executed recently.
    time (`datetime`_):

       The time when the action was executed.
