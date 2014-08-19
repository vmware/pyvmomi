
vim.host.SystemSwapConfiguration.DatastoreOption
================================================
  Use option to indicate that a user specified datastore may be used for system swap.
:extends: vim.host.SystemSwapConfiguration.SystemSwapOption_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    datastore (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The datastore to be used with this swap option. This value should be always set when the encapsulating option is used, otherwise a call to `UpdateSystemSwapConfiguration <vim/HostSystem.rst#updateSystemSwapConfiguration>`_ will result in a `InvalidArgument <vmodl/fault/InvalidArgument.rst>`_ fault.
