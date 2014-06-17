.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Description: ../../vim/Description.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _DiagnosticManagerLogFormat: ../../vim/DiagnosticManager/LogDescriptor/Format.rst

.. _DiagnosticManagerLogCreator: ../../vim/DiagnosticManager/LogDescriptor/Creator.rst


vim.DiagnosticManager.LogDescriptor
===================================
  Describes a log file that is available on a server.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       A key to identify the log file for browsing and download operations.
    fileName (`str`_):

       The filename of the log.
    creator (`str`_):

       The application that generated the log file. For more information on currently supported creators, see `DiagnosticManagerLogCreator`_ .
    format (`str`_):

       Describes the format of the log file. For more information on currently supported formats, see `DiagnosticManagerLogFormat`_ .
    mimeType (`str`_):

       Describes the mime-type of the returned file. Typical mime-types include:
        * text/plain - for a plain log file
    info (`vim.Description`_):

       Localized description of log file.
