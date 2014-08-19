
vim.host.PatchManager.Locator
=============================
  
:extends: vmodl.DynamicData_

Attributes:
    url (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The URL that will be used to access the patch repository.
    proxy (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The proxy setting required to access the URL from the host. If unset, a direct URL connection will be attempted.
