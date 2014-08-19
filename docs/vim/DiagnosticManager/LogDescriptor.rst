
vim.DiagnosticManager.LogDescriptor
===================================
  Describes a log file that is available on a server.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A key to identify the log file for browsing and download operations.
    fileName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The filename of the log.
    creator (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The application that generated the log file. For more information on currently supported creators, see `DiagnosticManagerLogCreator <vim/DiagnosticManager/LogDescriptor/Creator.rst>`_ .
    format (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Describes the format of the log file. For more information on currently supported formats, see `DiagnosticManagerLogFormat <vim/DiagnosticManager/LogDescriptor/Format.rst>`_ .
    mimeType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Describes the mime-type of the returned file. Typical mime-types include:
        * text/plain - for a plain log file
    info (`vim.Description <vim/Description.rst>`_):

       Localized description of log file.
