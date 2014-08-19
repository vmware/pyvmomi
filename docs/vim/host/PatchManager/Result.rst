
vim.host.PatchManager.Result
============================
  The result of the operation. Some of the fields are only valid for specific operations.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The version of the scan result schema.
    status ([`vim.host.PatchManager.Status <vim/host/PatchManager/Status.rst>`_], optional):

       The scan results for each patch.
    xmlResult (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The scan results in XML format.
