.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.DiagnosticManager.LogHeader
===============================
  A header that is returned with a set of log entries. This header describes where entries are located in the log file. Log files typically grow dynamically, so indexes based on line numbers may become inaccurate.
:extends: vmodl.DynamicData_

Attributes:
    lineStart (`int`_):

       The first line of this log segment.
    lineEnd (`int`_):

       The last line of this log segment.
    lineText ([`str`_], optional):

       Log entries, listed by line, for this log segment.
