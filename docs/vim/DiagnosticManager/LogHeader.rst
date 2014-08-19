
vim.DiagnosticManager.LogHeader
===============================
  A header that is returned with a set of log entries. This header describes where entries are located in the log file. Log files typically grow dynamically, so indexes based on line numbers may become inaccurate.
:extends: vmodl.DynamicData_

Attributes:
    lineStart (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The first line of this log segment.
    lineEnd (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The last line of this log segment.
    lineText ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Log entries, listed by line, for this log segment.
