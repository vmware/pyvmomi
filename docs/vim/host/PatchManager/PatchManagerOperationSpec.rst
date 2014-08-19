
vim.host.PatchManager.PatchManagerOperationSpec
===============================================
  Optional parameters for hostd to pass to exupdate.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    proxy (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The name of the possible proxy for esxupdate to use to connect to a server. The patch and metadata may be cached within the proxy server.
    port (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The port of the possible proxy for esxupdate to use to connect to a server. The patch and metadata may be cached within the proxy server.
    userName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The user name used for the proxy server.
    password (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The password used for the proxy server. This is passed with ssl through a trusted channel.
    cmdOption (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Possible command line options when calling esxupdate.
