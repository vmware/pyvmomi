
vim.host.CacheConfigurationManager.CacheConfigurationInfo
=========================================================
  Host solid state drive cache configuration information.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    key (`vim.Datastore <vim/Datastore.rst>`_):

       Datastore used for swap performance enhancements.
    swapSize (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Space allocated on this datastore to implement swap performance enhancements, in MB.
