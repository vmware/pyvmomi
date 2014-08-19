
vim.DiagnosticManager.BundleInfo
================================
  Describes a location of a diagnostic bundle and the server to which it belongs. This is a return type for the generateLogBundles operation.
:extends: vmodl.DynamicData_

Attributes:
    system (`vim.HostSystem <vim/HostSystem.rst>`_, optional):

       The host to which this diagnostic bundle belongs. If this is for the default server, then it is not set.
    url (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The location from which the diagnostic bundle can be downloaded. The host part of the URL is returned as '*' if the hostname to be used is the name of the server to which the call was made. For example, if the call is made to vcsrv1.domain1.com, and the bundle is available for download from http://vcsrv1.domain1.com/diagnostics/bundle.zip, the URL returned may be http:// * /diagnostics/bundle.zip. The client replaces the asterisk with the server name on which it invoked the call.
